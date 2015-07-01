# Module for prime numbers related functionality

# Tests if a given number 'n' is a strong pseudoprime or not, using
# the Rabin-Miller primality test.
#
# Will try as many bases as the specified 'k'. Note that the chance
# of flagging a number as pseudoprime when it is composite is 1/4^k,
# which quickly becomes more reliable than a deterministic test on
# hardware: http://stackoverflow.com/a/4160517/395386
#
# For an explanation of the algorithm, see '../text/Rabin-Miller.md'.
def is_prime_rabin_miller(n, k=40):
    return False #TODO

# Returns a random prime number with the given amount of bits.
def random_prime(bits):
    return 3 #TODO
