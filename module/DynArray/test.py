import unittest
from . import DynArray as arr


class test_DynArray(unittest.TestCase):

    '''
    Тест проверки метода на добавьте метод insert(i, itm),
    который вставляет в i-ю позицию объект itm,
    сдвигая вперёд все последующие элементы. Учитывая,
    что новая длина массива может превысить размер буфера.
    '''
    def test_insert(self):
        test1 = arr.DynArray()
        test1.append(25)
        test1.append(78)
        test1.append(2)
        test1.append(33)
        test1.append(245)
        test1.append(8)
        test1.insert(3, 88)

        self.assertEqual(test1[3], 88)  # проверка на key=3 => value=8
        self.assertEqual(test1[4], 33)  # проверка на key=4 => value=33
        self.assertEqual(len(test1), 7) # проверка длины массива
        self.assertEqual(test1.capacity, 16) # проверка на ёмкость буфера
        test1.append(52)
        for u in range(10):
            test1.append(u)
        self.assertEqual(len(test1), 18)    # проверка длины массива и должен был увеличиться буфер
        self.assertEqual(test1.capacity, 32)    # проверка на ёмкость буфера, должен увеличиться в 2х раза
        self.assertEqual(test1[17], 9)  # проверка на key=17 => value=9
        self.assertIsNone(test1.insert(55, 25)) #   Проверка на отсутствие в массиве key = 55

    def test_delete(self):
        test2 = arr.DynArray()
        test2.append(45)
        test2.append(12)
        test2.append(72)
        test2.append(5)
        test2.append(20)
        test2.append(98)
        test2.delete(3)
        self.assertEqual(test2[3], 20)  # проверка на key=3 => value=20
        self.assertEqual(len(test2), 5) # проверка длины массива
        test2.append(89)
        self.assertEqual(test2[5], 89)  # проверка на key=5 => value=89
        self.assertEqual(test2.capacity, 16)    # проверка на ёмкость буфера
        for i in range(11):
            test2.append(i)
        self.assertEqual(len(test2), 17)    # проверка длины массива
        self.assertEqual(test2.capacity, 32)    # проверка на ёмкость буфера
        test2.delete(2)

        '''
            проверка на ёмкость буфера, если длина массива
            len(test2) == test2.capacity
            то буфер должен увеличиться в 2х раза
        '''
        self.assertNotEqual(test2.capacity, 16)  # => True
        test2.delete(58)
        self.assertEqual(len(test2), 16)  # проверка длины массива

        '''
            проверка на ёмкость буфера, 
            должен уменьшиться в 2х раза, при условии:
            (test2.capacity / 2) > test2.count and test2.capacity > 16
        
        '''
        self.assertEqual(test2.capacity, 32) # => True

        '''
            Проверка на удаление элемента в недопустимой позиции 99 
        '''

        self.assertEqual(test2.delete(99), None) # test2.delete(99) => None, => True


if __name__ == '__main__':
    unittest.main()
