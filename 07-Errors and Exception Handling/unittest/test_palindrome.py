from palindrome import is_palindrome
from unittest import TestCase, main


class TestPalindrome(TestCase):

    def test_normal_string(self):
        self.assertEqual(is_palindrome("shubhamahbuhs"), True)
        self.assertEqual(is_palindrome("Meera"), False)
        self.assertEqual(is_palindrome("race car"), True)

    def test_empty_string(self):
        self.assertEqual(is_palindrome(""), True)

    def test_string_with_nums(self):
        self.assertEqual(is_palindrome("1234321"), True)
        self.assertEqual(is_palindrome("1234567"), False)

    def test_case_insensitive(self):
        self.assertEqual(is_palindrome("Race car"), True)


if __name__ == "__main__":
    main()
