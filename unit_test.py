import count_uniq_symb as cus
import unittest

cases = [(11234, False), ('abaabbcd1cc', False), ('11112334', 4)]


class Uniquetest(unittest.TestCase):
    def test_uniq(self):
        for arg1, arg2 in cases:
            self.assertEqual(cus.unique_symbols(arg1), arg2)


if __name__ == '__main__':
    unittest.main()
