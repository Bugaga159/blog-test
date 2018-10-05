import unittest
import doubly



class TestDoubleLinkedList(unittest.TestCase):

    # Тест проверки на удаление из списка узла
    def test_remove(self):
        test_rem =doubly.LinkedList2()
        test_rem.add_in_tail(doubly.Node2(1))
        test_rem.add_in_tail(doubly.Node2(2))
        test_rem.add_in_tail(doubly.Node2(3))
        test_rem.add_in_tail(doubly.Node2(4))
        test_rem.add_in_tail(doubly.Node2(5))

        test_rem.remove(4)
        res1 = test_rem.return_Lists()
        # Проверка res1 is not None
        self.assertIsNotNone(res1)

        # Проверка на соответствие, при удаление узла со значение 4
        self.assertEqual(res1, [['None', 1, 2],
                                [1, 2, 3],
                                [2, 3, 5],
                                [3, 5, 'None']])

        test_rem.remove(1)
        self.assertEqual(test_rem.head.value, 2)
        self.assertEqual(test_rem.head.next.value, 3)

        test_rem.remove(5)
        self.assertEqual(test_rem.tail.value, 3)
        self.assertIsNone(test_rem.tail.next)
        self.assertIsNotNone(test_rem.tail.prev)
        self.assertEqual(test_rem.tail.prev.value, 2)
        self.assertIsNone(test_rem.head.prev)

        test_rem.remove(3)
        res2 = test_rem.return_Lists()

        # Проверка на соответствие, при удаление всех узлов, кроме
        self.assertEqual(res2, [['None', 2, 'None']])



    # тест проверки метода вставки узла после заданного узла.
    def test_add_val_after(self):
        test_add = doubly.LinkedList2()
        test_add.add_in_tail(doubly.Node2(7))
        test_add.add_in_tail(doubly.Node2(8))
        test_add.add_in_tail(doubly.Node2(9))

        test_add.add_val_after(7, 42)
        res1 = test_add.return_Lists()
        self.assertEqual(res1, [['None', 7, 42],
                                [7, 42, 8],
                                [42, 8, 9],
                                [8, 9, 'None']])

        self.assertEqual(test_add.head.prev, None)
        self.assertIsNone(test_add.head.prev)
        self.assertEqual(test_add.head.next.value, 42)

        test_add.add_val_after(42, 16)
        res2 = test_add.return_Lists()
        self.assertEqual(res2, [['None', 7, 42],
                                [7, 42, 16],
                                [42, 16, 8],
                                [16, 8, 9],
                                [8, 9, 'None']])

        test_add.add_val_after(9, 64)
        self.assertEqual(test_add.tail.value, 64)
        self.assertEqual(test_add.tail.prev.value, 9)
        self.assertIsNone(test_add.tail.next)


    # тест проверки метода вставки узла самым первым элементом
    def test_add_first(self):
        test_add = doubly.LinkedList2()
        test_add.add_in_tail(doubly.Node2(2))
        test_add.add_in_tail(doubly.Node2(12))
        test_add.add_in_tail(doubly.Node2(74))

        test_add.add_first(52)
        res1 = test_add.return_Lists()
        self.assertEqual(res1, [['None', 52, 2],
                                [52, 2, 12],
                                [2, 12, 74],
                                [12, 74, 'None']])
        test_add.add_first(6)
        res2 = test_add.return_Lists()
        self.assertEqual(res2, [['None', 6, 52],
                                [6, 52, 2],
                                [52, 2, 12],
                                [2, 12, 74],
                                [12, 74, 'None']])