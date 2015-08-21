import primes
import random, math, unittest

class TestPrimes(unittest.TestCase):
    big_prime = 121999492637070040497464880653482451122159715698431661862504934268987469885677710797799523307422120568454593141727668682332216679465216347609718241998150443969871262326615939878834844507147192404574401325870276945218845272041195113380201145626974399759092850500988371156171063899568397919181947787377580179491
    big_not_prime = big_prime + 2

    def test_random_prime_1024_bits(self):
        random.seed(42)

        prime = primes.random_prime(random, 1024)
        self.assertEqual(1024, math.ceil(math.log(prime, 2)))
        self.assertTrue(primes.is_prime(random, prime))

    def test_prime_1024_bits(self):
        self.assertTrue(primes.is_prime(random, self.big_prime))

    def test_rabin_miller_1024_bits(self):
        self.assertTrue(primes.is_prime_miller_rabin(random, self.big_prime))

    def test_not_prime_1024_bits(self):
        self.assertFalse(primes.is_prime(random, self.big_not_prime))

    def test_not_rabin_miller_1024_bits(self):
        self.assertFalse(primes.is_prime_miller_rabin(random, self.big_not_prime))
