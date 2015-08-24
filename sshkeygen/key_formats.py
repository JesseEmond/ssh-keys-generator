"""Helper module to produce public/private keys output for SSH RSA keys.
    Functions:
        private_key_blob(params) --- produces the DER ASN1 blob for a PKCS#1
                                     private key from the given RsaParams.
        public_key_blob(params) --- produces the PEM encoded blob for an OpenSSH
                                    public key from the given RsaParams.
        private_key(params) --- produces the PKCS#1 private key format
                                from the given RsaParams.
        public_key(params) --- produces the OpenSSH public key format
                               from the given RsaParams.

    Note: for learning purposes, should normally use
          lib such as http://pyasn1.sourceforge.net/ .
"""

def private_key_blob(params):
    #TODO
    pass

def public_key_blob(params):
    #TODO
    pass

def private_key(params):
    #TODO
    pass

def public_key(params):
    #TODO
    pass
