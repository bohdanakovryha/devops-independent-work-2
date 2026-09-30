import unittest
from itertools import islice

from src.generator import even_odd_generator


class TestEvenOddGenerator(unittest.TestCase):
    def test_alternates(self):
        self.assertEqual(
            list(islice(even_odd_generator(), 5)),
            ["Even", "Odd", "Even", "Odd", "Even"],
        )

    def test_limit(self):
        self.assertEqual(list(even_odd_generator(4)), ["Even", "Odd", "Even", "Odd"])

    def test_zero_limit(self):
        self.assertEqual(list(even_odd_generator(0)), [])


if __name__ == "__main__":
    unittest.main()