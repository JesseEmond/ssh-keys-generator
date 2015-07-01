import unittest
import primes
import random, math

class TestPrimes(unittest.TestCase):
    def test_random_prime_1024(self):
        random.seed(42)

        for i in range(1000):
            prime = primes.random_prime(random, 1024)
            self.assertEqual(1024, math.ceil(math.log(prime, 2)))
            self.assertTrue(primes.is_prime_rabin_miller(prime))

