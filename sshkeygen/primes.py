"""Module for prime numbers related functionality

    Functions:
        is_prime --- checks if a number is prime (with a % of error)
        is_prime_miller_rabin -- checks if a number is a pseudoprime
        random_prime --- generates a random prime
"""


def is_prime(random, number):
    """Checks if a 'number' is prime, using 'random' to generate values
    used in probability primality tests.

    Assumes that 'number' is a relatively large number (above hundreds).
    """
    assert(number > _SMALL_PRIMES[-1])
    if number & 1 == 0: return False # even number

    # check for small primes (optimization)
    if any([factor for factor in _SMALL_PRIMES if number % factor == 0]):
        return False

    return is_prime_miller_rabin(random, number)

def is_prime_miller_rabin(random, number, iterations=40):
    """Tests if a given 'number' is a strong pseudoprime or not, using
    the Miller-Rabin primality test.

    Assumes that 'number' is odd.

    Will try as many bases as the specified 'iterations'. Note that the chance
    of flagging a number as pseudoprime when it is composite is 1/4^k,
    which quickly becomes reliable enough compared to a deterministic test on
    hardware: http://stackoverflow.com/a/4160517/395386

    For an explanation of the algorithm, see comments on
    https://github.com/JesseEmond/benchmarkus-prime/blob/master/primes.py
    """
    assert(number & 1 == 1)
    # get the form n - 1 = 2^s * d
    s = 0
    d = number - 1
    while d & 1 == 0: # is even
        d //= 2
        s += 1

    # try as many bases as 'iterations'
    for i in range(iterations):
        a = random.randrange(2, number)
        x = pow(a, d, number)
        if x == 1: # pseudoprime
            continue
        skip = False
        for r in range(s):
            if x == number - 1: # pseudoprime
                skip = True
                break
            x = pow(x, 2, number)

        if not skip:
            return False # composite

    return True

def random_prime(random, bits):
    """Returns a random prime number with the given amount of 'bits'.
    Uses the given 'random' generator.
    """
    while True:
        val = random_odd_number(random, bits)

        if is_prime(random, val):
            return val

def random_odd_number(random, bits):
    """Returns a random odd number with the given amount of 'bits'."""
    min_val = pow(2, bits - 1) + 1
    max_val = pow(2, bits) - 1
    return random.randrange(min_val, max_val, 2)


"""
List of small primes (ordered) that can be used to optimize primality
tests
"""
_SMALL_PRIMES = [ 3,  5,  7,
                 11, 13, 17,
                 19, 23, 29,
                 31, 37, 41,
                 43, 47, 53,
                 59, 61, 67,
                 71, 73, 79,
                 83, 89, 97]
