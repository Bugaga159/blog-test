import unittest
import LinkedList


class TestMain(unittest.TestCase):


    # Тест на проверкудобавление в список
    def test_return_all_nodes(self):
        test1 = main.LinkedList()

        # тест на проверку head = None
        self.assertIsNone(test1.head)

        test1.add_in_tail(main.Node(35))
        ran = test1.return_all_nodes()

        #тест на проверку данных в списке
        self.assertEquals(ran, [35])

        # тест на проверку head != None
        self.assertIsNotNone(test1.head)

    # тест на проверку данных в списке
    def test_remove(self):
        test1 = main.LinkedList()
        test1.add_in_tail(main.Node(35))
        test1.add_in_tail(main.Node(54))
        test1.add_in_tail(main.Node(35))
        test1.add_in_tail(main.Node(64))
        test1.remove(54)
        test1.remove(64)
        ran = test1.return_all_nodes()

        self.assertEquals(ran, [35, 35])

    # Тест проверяет, удалены ли все заданные значение, при вызове метода removeAllVal()
    def test_removeAllVal(self):
        test1 = main.LinkedList()
        test1.add_in_tail(main.Node(35))
        test1.add_in_tail(main.Node(54))
        test1.add_in_tail(main.Node(35))
        test1.add_in_tail(main.Node(64))
        test1.removeAllVal(35)
        test1.removeAllVal(64)
        ran = test1.return_all_nodes()

        self.assertEquals(ran, [54])

    # Тест проверяет, на пустоту  связанного списка
    def test_clearAll(self):
        test1 = main.LinkedList()
        test1.add_in_tail(main.Node(35))
        test1.add_in_tail(main.Node(54))
        res = test1.clearAll()

        self.assertEquals(res, None)
        self.assertIsNone(res)

    # Тест на поиск в списке
    def test_findVal(self):
        test1 = main.LinkedList()
        test1.add_in_tail(main.Node(35))
        test1.add_in_tail(main.Node(54))
        test1.add_in_tail(main.Node(35))
        test1.add_in_tail(main.Node(12))
        res1 = test1.findVal(35)
        res2 = test1.findVal(14)

        self.assertEquals(res1, [[35, 1], [35, 3]])
        self.assertEquals(res2, [])

    # Тест на определения длины списка
    def test_lengthList(self):
        test1 = main.LinkedList()
        test1.add_in_tail(main.Node(35))
        test1.add_in_tail(main.Node(54))
        test1.add_in_tail(main.Node(35))
        test1.add_in_tail(main.Node(64))
        res = test1.lengthList()

        self.assertEquals(res, 4)
        self.assertIsNotNone(res)

    # Тест на добавление значение, после заданного  значения
    def test_add_val_after(self):
        test1 = main.LinkedList()
        test1.add_in_tail(main.Node(35))
        test1.add_in_tail(main.Node(54))
        test1.add_in_tail(main.Node(35))
        test1.add_in_tail(main.Node(64))
        test1.add_val_after(35, 75)
        res1 = test1.return_all_nodes()
        self.assertEquals(res1, [35, 75, 54, 35, 64])
        test1.add_val_after(64, 75)
        res2 = test1.return_all_nodes()
        self.assertEquals(res2, [35, 75, 54, 35, 64, 75])

    '''
    Тест на проверку функцию, которая получает на вход
     два связанных списка, состоящие из целых значений, 
     и если их длины равны, возвращает список, каждый 
     элемент которого равен сумме соответствующих элементов 
     входных списков.
    '''
    def test_Comparison(self):
        test1 = main.LinkedList()
        test2 = main.LinkedList()
        test1.add_in_tail(main.Node(35))
        test1.add_in_tail(main.Node(54))
        test2.add_in_tail(main.Node(35))
        test2.add_in_tail(main.Node(64))

        res = main.Comparison(test1, test2)
        self.assertEquals(res, [70, 118])


if __name__ == "__main__":
    unittest.main()
