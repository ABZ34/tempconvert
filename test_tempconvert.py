import unittest

from tempconvert import c_to_f, c_to_k, convert, f_to_c, f_to_k, k_to_c, k_to_f


class TestCelsiusFahrenheit(unittest.TestCase):
    def test_c_to_f_freezing(self):
        self.assertAlmostEqual(c_to_f(0), 32)

    def test_c_to_f_boiling(self):
        self.assertAlmostEqual(c_to_f(100), 212)

    def test_f_to_c_freezing(self):
        self.assertAlmostEqual(f_to_c(32), 0)

    def test_f_to_c_boiling(self):
        self.assertAlmostEqual(f_to_c(212), 100)


class TestKelvin(unittest.TestCase):
    def test_c_to_k_freezing(self):
        self.assertAlmostEqual(c_to_k(0), 273.15)

    def test_k_to_c_absolute_zero(self):
        self.assertAlmostEqual(k_to_c(0), -273.15)

    def test_f_to_k_freezing(self):
        self.assertAlmostEqual(f_to_k(32), 273.15)

    def test_k_to_f_absolute_zero(self):
        self.assertAlmostEqual(k_to_f(0), -459.67)


class TestConvert(unittest.TestCase):
    def test_same_unit_returns_input(self):
        self.assertEqual(convert(50, "c", "c"), 50)

    def test_convert_c_to_k(self):
        self.assertAlmostEqual(convert(0, "c", "k"), 273.15)

    def test_unsupported_conversion_raises(self):
        with self.assertRaises(ValueError):
            convert(50, "x", "c")


if __name__ == "__main__":
    unittest.main()
