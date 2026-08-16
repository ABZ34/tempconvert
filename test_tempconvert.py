import unittest

from tempconvert import c_to_f, convert, f_to_c


class TestCelsiusFahrenheit(unittest.TestCase):
    def test_c_to_f_freezing(self):
        self.assertAlmostEqual(c_to_f(0), 32)

    def test_c_to_f_boiling(self):
        self.assertAlmostEqual(c_to_f(100), 212)

    def test_f_to_c_freezing(self):
        self.assertAlmostEqual(f_to_c(32), 0)

    def test_f_to_c_boiling(self):
        self.assertAlmostEqual(f_to_c(212), 100)


class TestConvert(unittest.TestCase):
    def test_same_unit_returns_input(self):
        self.assertEqual(convert(50, "c", "c"), 50)

    def test_unsupported_conversion_raises(self):
        with self.assertRaises(ValueError):
            convert(50, "x", "c")


if __name__ == "__main__":
    unittest.main()
