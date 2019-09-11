import unittest
from .solution import is_unique


class Test(unittest.TestCase):
    def test_not_unique(self):
        self.assertFalse(is_unique("paralelepipedo"))

    def test_unique(self):
        self.assertTrue(is_unique("murcielago"))


if __name__ == "__main__":
    unittest.main()
