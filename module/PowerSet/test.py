import unittest

from . import PowerSet

class TestPowerSet(unittest.TestCase):

    def test_put(self):
        test = PowerSet.PowerSet(17, 3)
        a = test.hash_fun(0)

        # символ - 0, в Юникоде в десятичной системе исчисления равен 48
        b = 48 % test.size

        self.assertEqual(b, a)

        c = test.hash_fun('a')
        # символ - a, в Юникоде в десятичной системе исчисления равен 48
        d = 97 % test.size
        self.assertEqual(d, c)

        # проверка на добавление в множество значен6ие, которое уже есть

        self.assertIsNone(test.put(0))

    def test_remove(self):
        test = PowerSet.PowerSet(17, 3)
        test.put(753)
        test.put(541)
        test.put(2)
        test.put('jhf')
        test.put(32)
        test.put('Hello')

        # проверка на удаление элемента
        a = test.find('Hello')
        self.assertEqual('Hello', test.slots[a])
        test.remove('Hello')
        self.assertIsNone(test.slots[a])

    def test_intersection(self):
        test1 = PowerSet.PowerSet(17, 3)
        test2 = PowerSet.PowerSet(17, 3)

        test1.put(15)
        test1.put(0)
        test1.put('a')
        test1.put('Y56')

        test2.put(0)
        test2.put(55)
        test2.put('Y56')
        test2.put('A')
        a = ['Y56', 0]
        self.assertEqual(a, test1.intersection(test2.slots))

        print(test2.remove(0))
        test2.remove('Y56')
        b = []
        print((test2.slots))
        self.assertEqual(b, test1.intersection(test2.slots))
