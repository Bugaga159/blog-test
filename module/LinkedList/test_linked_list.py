import unittest
from . import LinkedList


class TestMain(unittest.TestCase):

    # Тест на проверкудобавление в список
    def test_return_all_nodes(self):
        test1 = LinkedList.LinkedList()

        # тест на проверку head = None
        self.assertIsNone(test1.head)

        test1.add_in_tail(LinkedList.Node(35))
        ran = test1.return_all_nodes()

        #тест на проверку данных в списке
        self.assertEqual(ran, [35])

        # тест на проверку head != None
        self.assertIsNotNone(test1.head)

    # тест на проверку данных в списке
    def test_remove(self):
        test1 = LinkedList.LinkedList()
        test1.add_in_tail(LinkedList.Node(35))
        test1.add_in_tail(LinkedList.Node(54))
        test1.add_in_tail(LinkedList.Node(35))
        test1.add_in_tail(LinkedList.Node(64))
        test1.delete(54)
        test1.delete(64)
        ran = test1.return_all_nodes()

        self.assertEqual(ran, [35, 35])

        test2 = LinkedList.LinkedList()
        test2.add_in_tail(LinkedList.Node(35))
        test2.delete(35)
        self.assertEqual(None, test2.head)
        self.assertEqual(None, test2.tail)

    # Тест проверяет, удалены ли все заданные значение, при вызове метода removeAllVal()
    def test_removeAllVal(self):
        test1 = LinkedList.LinkedList()
        test1.add_in_tail(LinkedList.Node(35))
        test1.add_in_tail(LinkedList.Node(54))
        test1.add_in_tail(LinkedList.Node(35))
        test1.add_in_tail(LinkedList.Node(64))
        test1.delete(35, True)
        test1.delete(64, True)
        ran = test1.return_all_nodes()

        self.assertEqual(ran, [54])

        test2 = LinkedList.LinkedList()
        test2.add_in_tail(LinkedList.Node(35))
        test2.add_in_tail(LinkedList.Node(35))
        test2.delete(35, True)
        self.assertEqual(None, test2.head)
        self.assertEqual(None, test2.tail)

    # Тест проверяет, на пустоту  связанного списка
    def test_clean(self):
        test1 = LinkedList.LinkedList()
        test1.add_in_tail(LinkedList.Node(35))
        test1.add_in_tail(LinkedList.Node(54))
        res = test1.clean()

        self.assertEqual(res, None)
        self.assertIsNone(res)

    # Тест на поиск в списке
    def test_find_all(self):
        test1 = LinkedList.LinkedList()

        res1 = test1.find_all(35)
        self.assertEqual([], res1)

        test1.add_in_tail(LinkedList.Node(35))
        test1.add_in_tail(LinkedList.Node(54))
        test1.add_in_tail(LinkedList.Node(35))
        test1.add_in_tail(LinkedList.Node(12))
        res2 = test1.find_all(35)
        res3 = test1.find_all(13)

        self.assertEqual(test1.head, res2[0])
        self.assertEqual([], res3)


    # Тест на определения длины списка
    def test_lengthList(self):
        test1 = LinkedList.LinkedList()
        test1.add_in_tail(LinkedList.Node(35))
        test1.add_in_tail(LinkedList.Node(54))
        test1.add_in_tail(LinkedList.Node(35))
        test1.add_in_tail(LinkedList.Node(64))
        res1 = test1.len()

        self.assertEqual(4, res1)

        test2 = LinkedList.LinkedList()
        res2 = test2.len()
        self.assertEqual(0, res2)


    # Тест на добавление значение, после заданного  значения
    def test_insert(self):
        test1 = LinkedList.LinkedList()
        res1 = test1.insert(94, 65)
        self.assertTrue(res1)
        self.assertEqual(65, test1.head.value)

        test1.add_in_tail(LinkedList.Node(35))
        test1.add_in_tail(LinkedList.Node(54))
        test1.add_in_tail(LinkedList.Node(35))
        test1.add_in_tail(LinkedList.Node(64))

        res2 = test1.insert(35, 75)
        self.assertTrue(res2)

        res3 = test1.insert(36, 75)
        self.assertFalse(res3)


    '''
    Тест на проверку функцию, которая получает на вход
     два связанных списка, состоящие из целых значений, 
     и если их длины равны, возвращает список, каждый 
     элемент которого равен сумме соответствующих элементов 
     входных списков.
    '''
    def test_Comparison(self):
        test1 = LinkedList.LinkedList()
        test2 = LinkedList.LinkedList()
        test1.add_in_tail(LinkedList.Node(35))
        test1.add_in_tail(LinkedList.Node(54))
        test2.add_in_tail(LinkedList.Node(35))
        test2.add_in_tail(LinkedList.Node(64))

        res = LinkedList.Comparison(test1, test2)
        self.assertEqual(70, res.head.value)
        self.assertEqual(118, res.tail.value)
