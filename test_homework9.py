from unittest import TestCase, mock
from Homework8 import account


class Test(TestCase):
    def test_example1(self):
        # valid withdrawl
        expected = 20
        with mock.patch("builtins.input", return_value=80): # this line mocks (i.e. pretends) that the input for "How much you'd like to withdraw" is 80.
            result = account()
        self.assertEqual(expected, result)


    def test_example2(self):
        # invalid withdrawl
        with mock.patch("builtins.input", return_value=150): # this line pretends that the input for "How much you'd like to withdraw" is 150.
            result = account()
        self.assertEqual("Insufficient funds", account())
