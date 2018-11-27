import unittest

from . import NativeDictionary

class TestNativeDictionary(unittest.TestCase):

    def test_hash_fun(self):
        test = NativeDictionary.HashTable(17, 3)
        a = test.hash_fun(0)

        # символ - 0, в Юникоде в десятичной системе исчисления равен 48
        b = 48 % test.size

        self.assertEqual(b, a)

        c = test.hash_fun('a')
        # символ - a, в Юникоде в десятичной системе исчисления равен 48
        d = 97 % test.size
        self.assertEqual(d, c)


    def test_seek_slot(self):
        test = NativeDictionary.HashTable(17, 3)
        a = test.seek_slot(0)
        # символ - 0, в Юникоде в десятичной системе исчисления равен 48
        b = 48 % test.size
        self.assertEqual(b, a)

        c = test.seek_slot('a')
        # символ - a, в Юникоде в десятичной системе исчисления равен 48
        d = 97 % test.size
        self.assertEqual(d, c)

    def test_put(self):
        test = NativeDictionary.HashTable(17, 3)
        test.put(9, '15932')
        test.put('Apple', 65)

        # Проверка на соответствие
        self.assertEqual('15932', test.dictionary[9])
        self.assertEqual(65, test.dictionary['Apple'])
        # Проверка на None, если ключ не правильный
        self.assertIsNone(test1.dictionary['apple'])

        # Меняем значение в словаре
        test.put('Apple', 50)
        self.assertEqual(50, test.dictionary['Apple'])

    def test_is_key(self):
        test = NativeDictionary.HashTable(17, 3)
        test.put(9, '15932')
        test.put('Apple', 65)

        self.assertTrue(test.is_key('Apple'))
        self.assertIsNone(test.is_key('apple'))

    def test_get(self):
        test = NativeDictionary.HashTable(17, 3)
        test.put(9, '15932')
        test.put('Apple', 65)

        self.assertEqual(65, test.get('Apple'))
        self.assertEqual('15932', test.get(9))

        # Меняем значение в словаре по ключу 
        test.put('Apple', 50)
        self.assertEqual(50, test.get('Apple'))
        self.assertIsNone(test.get('apple'))

