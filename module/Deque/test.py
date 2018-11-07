import unittest
from . import Deque

class TestDeque(unittest.TestCase):

    def test_addFront(self):
        test = Deque.Deque()

        # Проверки длины size() => 0
        self.assertEqual(test.size(), 0)
        test.addFront('f1')
        test.addFront('f2')

        # Проверки длины size() => 2
        self.assertEqual(test.size(), 2)

        # Проверка на наличие в Очереди значение
        self.assertIn('f2', test.queue)

    def test_addTail(self):
        test = Deque.Deque()

        # Проверки длины size() => 0
        self.assertEqual(test.size(), 0)
        test.addTail('t1')
        test.addTail('t2')

        # Проверки длины size() => 2
        self.assertEqual(test.size(), 2)

        # Проверка на наличие в Очереди значение
        self.assertIn('t2', test.queue)

    def test_removeFront(self):
        test = Deque.Deque()
        test.addFront('f1')
        test.addFront('f2')
        test.addFront('f3')

        # Проверки длины size() => 3
        self.assertEqual(test.size(), 3)
        # Удаляем значение в конце Очереди
        test.removeFront()

        # Проверки длины size() => 2
        self.assertEqual(test.size(), 2)

        # Проверка на наличие в Очереди значение => False
        self.assertNotIn('f3', test.queue)

    def test_removeTail(self):
        test = Deque.Deque()
        test.addTail('t1')
        test.addTail('t2')
        test.addTail('t3')

        # Проверки длины size() => 3
        self.assertEqual(test.size(), 3)

        # Удаляем значение в начале Очереди
        test.removeTail()

        # Проверки длины size() => 2
        self.assertEqual(test.size(), 2)

        # Проверка на наличие в Очереди значение => False
        self.assertNotIn('t3', test.queue)



