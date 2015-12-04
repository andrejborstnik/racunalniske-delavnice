import binary
import unittest

class TestBinary(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(binary.to_binary(0), '0')

    def test_positive(self):
        self.assertEqual(binary.to_binary(1), '1')
        self.assertEqual(binary.to_binary(True), '1')
        self.assertEqual(binary.to_binary(2), '10')
        self.assertEqual(binary.to_binary(4), '100')
        self.assertEqual(binary.to_binary(6), '110')

    ## @unittest.skip('Depreciated.')
    def test_negative(self):
        self.assertEqual(binary.to_binary(-5), '-101')
        self.assertEqual(binary.to_binary(-10), '-1010')
        self.assertEqual(binary.to_binary(False), '0')

    def test_invalid(self):
        self.assertRaisesRegex(TypeError, "Argument must be an integer.", binary.to_binary, 1.6)
        self.assertRaisesRegex(TypeError, "Argument must be an integer.", binary.to_binary, '23')
        self.assertRaisesRegex(TypeError, "Argument must be an integer.", binary.to_binary, [12])

if __name__ == '__main__':
    unittest.main()
