import unittest
from cdiscount_robin_clementine.price_parser import parse_price

class TestPriceParser(unittest.TestCase):
    def test_isStringParam(self):
        result = parse_price('sur4444888884974')
        self.assertEqual(result, 29.37)

if __name__ == '__main__':
    unittest.main()
