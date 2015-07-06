# Module for prime numbers related functionality


# Checks if a 'number' is prime.
def is_prime(number):
    if number <= 1: return False
    if number == 2: return True
    if number & 1 == 0: return False

    #TODO test against small primes here

    return is_prime_rabin_miller(number)

# Tests if a given 'number' is a strong pseudoprime or not, using
# the Rabin-Miller primality test.
#
# Assumes that 'number' is odd.
#
# Will try as many bases as the specified 'iterations'. Note that the chance
# of flagging a number as pseudoprime when it is composite is 1/4^k,
# which quickly becomes more reliable than a deterministic test on
# hardware: http://stackoverflow.com/a/4160517/395386
#
# For an explanation of the algorithm, see '../text/Rabin-Miller.md'.
def is_prime_rabin_miller(number, iterations=40):

    return False #TODO

# Returns a random prime number with the given amount of 'bits'.
# Uses the given 'random' generator.
def random_prime(random, bits):

    return 3 #TODO
