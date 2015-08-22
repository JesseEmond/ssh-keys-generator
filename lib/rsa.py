"""Functionality related to the RSA encryption algorithm.
    Classes:
        RsaParams --- RSA public/private precalculated parameters
"""

from modular_arithmetic import mod_inv

class RsaParams(object):
    """RSA public/private precalculated parameters, calculated from
    the given public/private exponent.

    Attributes:
        prime1 --- first private prime number ("p")
        prime2 --- second private prime number ("q")
        modulus --- public modulus ("n")
        publicExponent --- public exponent ("e")
        privateExponent --- private exponent ("d")
        exponent1 --- d mod (p-1)
        exponent2 --- d mod (q-1)
        coefficient --- (inverse of q) mod p
    """

    def __init__(self, p, q):
        """Precalculates the parameters of the RSA configuration produced
        from the two given prime numbers.
        """

        n = p * q
        totient = (p - 1) * (q - 1)
        e = 65537
        assert(e < totient)
        d = mod_inv(e, totient)
        
        self.prime1 = p
        self.prime2 = q
        self.modulus = n
        self.publicExponent = e
        self.privateExponent = d
        self.exponent1 = d % (p - 1)
        self.exponent2 = d % (q - 1)
        self.coefficient = mod_inv(q, p)
