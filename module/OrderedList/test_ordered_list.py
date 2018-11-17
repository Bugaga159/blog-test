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

    def test_search(self):
        test = OrderedList()
        test.add_in_tail(Node(45))
        test.add_in_tail(Node(23))
        test.add_in_tail(Node(167))
        test.add_in_tail(Node(46))
        test.add_in_tail(Node(71))
        self.assertEqual(test.head.value, 23)
        self.assertTrue(test.search(167))
        self.assertTrue(test.search(45))
        self.assertFalse(test.search(72))

    def test_arr(self):
        test = OrderedList()
        test.add_in_tail(Node(45))
        test.add_in_tail(Node(23))
        test.add_in_tail(Node(167))
        test.sortArr()
        self.assertEqual([23, 45, 167], test.array)

        test.sortArr(1)
        self.assertEqual([167, 45, 23], test.array)


class TestCompSTR(unittest.TestCase):

    def test_add_in_tail(self):
        test = СomparisonStrings()
        test.add_in_tail(Node('hello'))
        test.add_in_tail(Node('  who are you'))
        test.add_in_tail(Node(' bay!  '))

        self.assertEqual('bay!', test.head.value)
        self.assertEqual('who are you', test.tail.value)

    def test_remove(self):
        test = СomparisonStrings()
        test.add_in_tail(Node('My name is Andrey'))
        test.add_in_tail(Node('Adress'))
        test.add_in_tail(Node('year'))

        self.assertEqual('Adress', test.head.value)
        self.assertEqual('year', test.tail.value)

        test.remove('Adress')
        self.assertEqual('My name is Andrey', test.head.value)

    def test_search(self):
        test = СomparisonStrings()
        test.add_in_tail(Node('Name'))
        test.add_in_tail(Node('Nomber'))
        test.add_in_tail(Node('Date'))

        self.assertTrue(test.search('Date'))
        self.assertFalse(test.search('date'))

    def test_arr(self):
        test = СomparisonStrings()
        test.add_in_tail(Node('Name'))
        test.add_in_tail(Node('Nomber'))
        test.add_in_tail(Node('Date'))

        test.sortArr()
        self.assertEqual(['Date', 'Name', 'Nomber'], test.array)

        test.sortArr(1)
        self.assertEqual(['Nomber', 'Name', 'Date'], test.array)
