import unittest
from . import doubly



class TestDoubleLinkedList(unittest.TestCase):
    # Тест на добавление в список
    def test_add_in_tail(self):
        test1 = doubly.LinkedList2()

        # тест на проверку head = None
        self.assertIsNone(test1.head)

        test1.add_in_tail(doubly.Node(35))

        # тест на проверку данных в списке
        self.assertEqual(35, test1.head.value)

        # тест на проверку head != None
        self.assertIsNotNone(test1.head)
        self.assertIsNotNone(test1.tail)

    # тест на проверку данных в списке
    def test_delete(self):
        test1 = doubly.LinkedList2()
        self.assertFalse(test1.delete(54))
        test1.add_in_tail(doubly.Node(35))
        test1.add_in_tail(doubly.Node(54))
        test1.add_in_tail(doubly.Node(35))
        test1.add_in_tail(doubly.Node(64))
        test1.delete(54)
        test1.delete(64)

        self.assertEqual(35, test1.head.value)
        self.assertEqual(35, test1.head.next.value)
        self.assertEqual(35, test1.head.next.prev.value)


        test2 = doubly.LinkedList2()
        test2.add_in_tail(doubly.Node(35))
        test2.delete(35)
        self.assertEqual(None, test2.head)
        self.assertEqual(None, test2.tail)


    # Тест проверяет, на пустоту  связанного списка
    def test_clean(self):
        test1 = doubly.LinkedList2()
        test1.add_in_tail(doubly.Node(35))
        test1.add_in_tail(doubly.Node(54))

        test1.clean()
        self.assertEqual(None, test1.head)
        self.assertIsNone(test1.tail)

    # Тест на поиск в списке
    def test_find(self):
        test1 = doubly.LinkedList2()

        res1 = test1.find(35)
        self.assertIsNone(res1)

        test1.add_in_tail(doubly.Node(35))
        test1.add_in_tail(doubly.Node(54))
        test1.add_in_tail(doubly.Node(35))
        test1.add_in_tail(doubly.Node(12))

        res2 = test1.find(35)
        self.assertEqual(35, res2.value)
        res3 = test1.find(13)
        self.assertEqual(None, res3)

    # Тест на определения длины списка
    def test_len(self):
        test1 = doubly.LinkedList2()
        test1.add_in_tail(doubly.Node(35))
        test1.add_in_tail(doubly.Node(54))
        test1.add_in_tail(doubly.Node(35))
        test1.add_in_tail(doubly.Node(64))
        res1 = test1.len()

        self.assertEqual(4, res1)

        test2 = doubly.LinkedList2()
        res2 = test2.len()
        self.assertEqual(0, res2)

    # Тест на добавление значение, после заданного  значения
    def test_insert(self):
        test1 = doubly.LinkedList2()

        # Новый узел для вставки
        newNode1 = doubly.Node(65)
        res1 = test1.insert(doubly.Node(12), newNode1)
        self.assertTrue(res1)
        self.assertEqual(65, test1.head.value)
        self.assertEqual(65, test1.tail.value)

        # Добавляем новые узлы в список
        test1.add_in_tail(doubly.Node(35))
        test1.add_in_tail(doubly.Node(54))
        test1.add_in_tail(doubly.Node(35))
        test1.add_in_tail(doubly.Node(64))

        # Новый узел для вставки
        newNode2 = doubly.Node(75)

        # Вставка узла в список с положительным ответом
        res2 = test1.insert(doubly.Node(54), newNode2)
        self.assertTrue(res2)

        # Вставка узла в список с отрицательным ответом
        res3 = test1.insert(doubly.Node(66), newNode2)
        self.assertFalse(res3)


if __name__ == "__main__":
    unittest.main()