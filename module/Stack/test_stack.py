import unittest
from . import Stack


class TestStack(unittest.TestCase):

    def test_pop_head(self):
        test1 = Stack.Stack()
        test1.push(35)
        test1.push(52)
        test1.push(8)

        self.assertEqual(test1.pop_head(), 35)

        self.assertEqual(test1.pop_head(), 52)
