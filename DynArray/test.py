import unittest
import DynArray as arr

class test_DynArray(unittest.TestCase):

    '''
    Тест проверки метода на добавьте метод insert(i, itm),
    который вставляет в i-ю позицию объект itm,
    сдвигая вперёд все последующие элементы. Учитывая,
    что новая длина массива может превысить размер буфера.
    '''
    def test_insert(self):
        da = arr.DynArray()
        for i in range(16):
            da.append(i)
        da.insert(3, 88)
        self.assertEqual(da[3], 88)
        self.assertEqual(da[4], 3)
        self.assertEqual(len(da), 17)
        self.assertEqual(da.capacity, 32)

