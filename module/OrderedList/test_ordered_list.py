import unittest
from .OrderedList import *

class TestOrderedList(unittest.TestCase):

    def test_add_in_tail(self):
        test = OrderedList()
        test.add_in_tail(Node(0))
        test.add_in_tail(Node(2))
        test.add_in_tail(Node(9))
        test.add_in_tail(Node(1))
        test.add_in_tail(Node(10))

        self.assertEqual(test.head.value, 0)

        self.assertEqual(test.head.next.value, 1)
        self.assertEqual(test.head.next.next.value, 2)
        self.assertEqual(test.head.next.next.next.value, 9)
        self.assertEqual(test.tail.value, 10)


    def test_remove(self):
        test = OrderedList()
        test.add_in_tail(Node(566))
        test.add_in_tail(Node(3))
        test.add_in_tail(Node(0))
        test.add_in_tail(Node(55))
        test.add_in_tail(Node(91))

        self.assertEqual(test.head.value, 0)

        test.remove(0)
        self.assertEqual(test.head.value, 3)
        self.assertEqual(test.tail.value, 566)

        test.remove(566)
        self.assertEqual(91, test.tail.value)
        self.assertEqual(91, test.head.next.next.value)