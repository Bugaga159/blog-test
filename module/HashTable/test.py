import unittest
from . import HashTable

class TestHashTable(unittest.TestCase):

    def test_hash_fun(self):
        test = HashTable.HashTable(17, 3)
        a = test.hash_fun(0)

        # символ - 0, в Юникоде в десятичной системе исчисления равен 48
        b = 48 % test.size

        self.assertEqual(b, a)

        c = test.hash_fun('a')
        # символ - a, в Юникоде в десятичной системе исчисления равен 48
        d = 97 % test.size
        self.assertEqual(d, c)

    def test_seek_slot(self):
        test = HashTable.HashTable(17, 3)
        a = test.seek_slot(0)
        # символ - 0, в Юникоде в десятичной системе исчисления равен 48
        b = 48 % test.size
        self.assertEqual(b, a)

        c = test.seek_slot('a')
        # символ - a, в Юникоде в десятичной системе исчисления равен 48
        d = 97 % test.size
        self.assertEqual(d, c)

    def test_put(self):
        test = HashTable.HashTable(17, 3)
        test.put(0)
        # символ - 0, в Юникоде в десятичной системе исчисления равен 48
        a = 48 % test.size
        self.assertEqual(0, test.slots[a])

        self.assertIsNone(test.put(0))

        test.put('a')
        b = 97 % test.size
        self.assertEqual('a', test.slots[b])

    def test_find(self):
        test = HashTable.HashTable(17, 3)
        test.put(0)
        a = 48 % test.size
        self.assertEqual(a, test.find(0))
        test.put('a')
        b = 97 % test.size
        self.assertEqual(b, test.find('a'))
        