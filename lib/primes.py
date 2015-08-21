# Module for prime numbers related functionality


# Checks if a 'number' is prime.
def is_prime(number):
    if number <= 1: return False
    if number == 2: return True
    if number & 1 == 0: return False

    return is_prime_miller_rabin(number)

# Tests if a given 'number' is a strong pseudoprime or not, using
# the Miller-Rabin primality test.
#
# Assumes that 'number' is odd.
#
# Will try as many bases as the specified 'iterations'. Note that the chance
# of flagging a number as pseudoprime when it is composite is 1/4^k,
# which quickly becomes reliable enough compared to a deterministic test on
# hardware: http://stackoverflow.com/a/4160517/395386
#
# For an explanation of the algorithm, see comments on
# https://github.com/JesseEmond/benchmarkus-prime/blob/master/primes.py
def is_prime_miller_rabin(random, number, iterations=40):
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

# Returns a random prime number with the given amount of 'bits'.
# Uses the given 'random' generator.
def random_prime(random, bits):

    while True:
        

    return 3 #TODO
