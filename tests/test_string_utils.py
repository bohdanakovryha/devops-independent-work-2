import io
import unittest
from contextlib import redirect_stdout

from src.string_utils import print_string, describe_case, upper_letters


class TestPrintString(unittest.TestCase):
    def test_prints_text(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            result = print_string("Hello")
        self.assertEqual(buffer.getvalue(), "Hello\n")
        self.assertEqual(result, "Hello")

    def test_not_a_string(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            result = print_string(42)
        self.assertIsNone(result)
        self.assertIn("Error: expected str, got int", buffer.getvalue())


class TestDescribeCase(unittest.TestCase):
    def run_quiet(self, value):
        with redirect_stdout(io.StringIO()):
            return describe_case(value)

    def test_uppercase(self):
        self.assertEqual(self.run_quiet("PYTHON"), "all uppercase")

    def test_lowercase(self):
        self.assertEqual(self.run_quiet("python"), "all lowercase")

    def test_mixed(self):
        self.assertEqual(self.run_quiet("PyThOn"), "mixed case")

    def test_no_letters(self):
        self.assertEqual(self.run_quiet("123"), "no letters")

    def test_not_a_string(self):
        self.assertIsNone(self.run_quiet(3.14))


class TestUpperLetters(unittest.TestCase):
    def test_smogtether(self):
        self.assertEqual(
            upper_letters("smogtether"),
            ["S", "M", "O", "G", "T", "E", "T", "H", "E", "R"],
        )

    def test_not_a_string(self):
        with redirect_stdout(io.StringIO()):
            self.assertIsNone(upper_letters(None))


if __name__ == "__main__":
    unittest.main()