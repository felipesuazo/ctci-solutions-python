import unittest
from .solution import check_permutation


class Test(unittest.TestCase):
    def test_is_permutation(self):
        self.assertTrue(check_permutation("calle", "lleca"))

    def test_is_not_permutation(self):
        self.assertFalse(check_permutation("calle", "falta"))


if __name__ == "__main__":
    unittest.main()