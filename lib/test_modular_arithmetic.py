import modular_arithmetic
import unittest

class TestModularArithmetic(unittest.TestCase):
    def test_egcd_17_5(self):
        gcd, a, b = modular_arithmetic.egcd(17,5)
        self.assertEqual(1, gcd)
        self.assertEqual(-2, a)
        self.assertEqual(7, b)
        
    def test_mod_inv_7_31(self):
        inv = modular_arithmetic.mod_inv(7,31)
        self.assertEqual(9, inv)

