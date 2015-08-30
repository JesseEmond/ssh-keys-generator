"""Module for prime numbers related functionality

    Functions:
        is_prime --- checks if a number is prime (with a % of error)
        is_prime_miller_rabin -- checks if a number is a pseudoprime
        random_prime --- generates a random prime
"""


def is_prime(random, number):
    """Checks if a 'number' is prime, using 'random' to generate values
    used in probability primality tests.

    Assumes that 'number' is greater than 100.
    """
    assert(number > 100)
    if number & 1 == 0: return False # even number

    # check for small primes (optimization)
    if number %  3 == 0 or number %  5 == 0 or number %  7 == 0 or \
       number % 11 == 0 or number % 13 == 0 or number % 17 == 0 or \
       number % 19 == 0 or number % 23 == 0 or number % 29 == 0 or \
       number % 31 == 0 or number % 37 == 0 or number % 41 == 0 or \
       number % 43 == 0 or number % 47 == 0 or number % 53 == 0 or \
       number % 59 == 0 or number % 61 == 0 or number % 67 == 0 or \
       number % 71 == 0 or number % 73 == 0 or number % 79 == 0 or \
       number % 83 == 0 or number % 89 == 0 or number % 97 == 0:
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
