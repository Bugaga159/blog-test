import unittest
from module.Queues import Queues
from module.Queues import QueuesStack as Stack

class TestQueues(unittest.TestCase):

    def test_enqueue(self):
        test1 = Queues.Queue()
        test1.enqueue(30)
        self.assertEqual(test1.items[0], 30)
        test1.enqueue(3)
        self.assertEqual(test1.items[0], 3)

    '''
        Тест проверки функции на вращение элементов в Очереди
    '''
    def test_rotation(self):
        test = Queues.Queue()
        for i in range(5):
            test.enqueue(i)

        # Сдвигаем элементы Очереди на 1 позицию по кругу
        # [ 4, 3, 2, 1, 0] => [1, 4, 3, 2, 1]
        items1 = test.items
        res = Queues.rotation(items1, 1)
        self.assertEqual(res[0], 0)

        # Сдвигаем элементы Очереди на 4 позицию по кругу
        # [1, 4, 3, 2, 1]=> [ 4, 3, 2, 1, 0]
        items2 = test.items
        res2 = Queues.rotation(items2, 1)
        self.assertEqual(res2[0], 4)


class TestQueuesThroughTheStack(unittest.TestCase):
    '''
        Тест на проверку создания "Очереди" через 2 "Стека".
    '''
    def test_enqueue(self):
        test = Stack.QueuesThroughTheStack()
        test.enqueue(12)
        test.enqueue(34)
        test.enqueue(81)
        test.enqueue(56)
        test.enqueue(78)

        # Проверка последнего элемента Очереди на соответствие
        # test.item.stack[0] == 78
        res1 = test.item.stack
        self.assertEqual(res1[0], 78)

        # Проверка первого элемента Очереди на соответствие
        # test.item.stack[4] == 12
        res2 = test.item.stack
        self.assertEqual(res2[4], 12)

    '''
        Тест на проверку вывода и удаления из "Очереди" первого элемента
    '''
    def test_dequeue(self):
        test = Stack.QueuesThroughTheStack()
        test.enqueue(58)
        test.enqueue(78)
        test.enqueue(65)
        test.enqueue(24)

        # test.item.stack[3] == 58
        self.assertEqual(test.dequeue(), 58)

        # test.item.stack[2] == 78
        self.assertEqual(test.dequeue(), 78)

    '''
        Тест на проверку длины "Очереди"
    '''
    def test_size(self):
        test = Stack.QueuesThroughTheStack()
        self.assertEqual(test.size(), 0)

        for i in range(10):
            test.enqueue(i)
        self.assertEqual(test.size(), 10)