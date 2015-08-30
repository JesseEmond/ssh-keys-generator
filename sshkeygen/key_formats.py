"""Helper module to produce public/private keys output for SSH RSA keys.
    Functions:
        private_key_blob(params) --- produces the DER ASN1 blob for a PKCS#1
                                     private key from the given RsaParams.
        public_key_blob(params) --- produces the PEM-encoded blob for an OpenSSH
                                    public key from the given RsaParams.
        private_key(params) --- produces the PKCS#1 private key format
                                from the given RsaParams.
        public_key(params) --- produces the OpenSSH public key format
                               from the given RsaParams.
"""

import struct, base64, math
from pyasn1.type import univ
from pyasn1.codec.der import encoder

class PrivateKeySequence(univ.SequenceOf):
    """ASN.1 sequence used for the private key format."""
    componentType = univ.Integer()

def private_key_blob(params):
    """Produces the PKCS#1 private key ASN1 blob of the precomputed RSA
    parameters.

    The key has the following ASN.1 structure:
    RSAPrivateKey ::= SEQUENCE {
        version           Version,
        modulus           INTEGER,  -- n
        publicExponent    INTEGER,  -- e
        privateExponent   INTEGER,  -- d
        prime1            INTEGER,  -- p
        prime2            INTEGER,  -- q
        exponent1         INTEGER,  -- d mod (p-1)
        exponent2         INTEGER,  -- d mod (q-1)
        coefficient       INTEGER,  -- (inverse of q) mod p
    }
    (source: https://tools.ietf.org/html/rfc3447#page-7)

    Returns the resulting DER-encoded blob base64-encoded.
    """
    seq = PrivateKeySequence()

    seq.setComponentByPosition(0, 0)
    seq.setComponentByPosition(1, params.modulus)
    seq.setComponentByPosition(2, params.publicExponent)
    seq.setComponentByPosition(3, params.privateExponent)
    seq.setComponentByPosition(4, params.prime1)
    seq.setComponentByPosition(5, params.prime2)
    seq.setComponentByPosition(6, params.exponent1)
    seq.setComponentByPosition(7, params.exponent2)
    seq.setComponentByPosition(8, params.coefficient)

    der = encoder.encode(seq)
    return base64.b64encode(der)

def encode_openssh_blob_data(data):
    """Encodes a single data chunk from the blob inserted in an OpenSSH key.

    The data is encoded as a length-data pair:
    - length of the data as 4 octets in big-endian order
    - the raw data 
    """
    length = struct.pack('>I', len(data))
    assert(len(length) == 4)

    return length + data

def encode_mpint(num):
    """Encodes an mpint, as defined by https://www.ietf.org/rfc/rfc4251.txt .
    Basically, this splits the number into its bytes (big-endian) and
    puts a leading 0 if necessary (if the most significant bit is set,
    as we only deal with unsigned integers in our context and don't want
    negative integers).
    """
    # Hackish, but does the job for now
    BYTE_SIZE = 256
    packed = bytearray()
    while num > 0:
        packed.append(num % BYTE_SIZE) 
        num //= BYTE_SIZE

    if packed[len(packed)-1] & 0x80 != 0: # sign-bit would be set? prepend 0.
        packed.append(0) # will be reversed

    packed.reverse() # put in netword-order
    return packed

def public_key_blob(params):
    """Produces the PEM-encoded blob of length-data pairs for an OpenSSH
    public key from the given RSA parameters.

    The key has the following data encoded:
    - algorithm used (ssh-rsa, ssh-dsa, ...)
    - public exponent (e)
    - modulus (n)

    Return a base64 of the resulting concatenation of the pairs.
    """

    algo = b'ssh-rsa'
    exponent = encode_mpint(params.publicExponent)
    modulus = encode_mpint(params.modulus)
    parts = [algo, exponent, modulus]

    raw = bytearray().join(map(encode_openssh_blob_data, parts))

    return base64.b64encode(raw)

def private_key(params):
    #TODO
    pass

def public_key(params, comment):
    """Produces the OpenSSH public key format from the RSA parameters and a key
    comment.
    Used http://blog.oddbit.com/2011/05/08/converting-openssh-public-keys/ as a
    resource.
    """
    keytype = 'ssh-rsa'
    blob = public_key_blob(params).decode('utf-8')

    return " ".join([keytype, blob, comment])
