import unittest
from . import Stack


class TestStack(unittest.TestCase):

    def test_pop_head(self):
        test1 = Stack.Stack()
        test1.push(35)
        test1.push(52)
        test1.push(8)

        #   Проверка метода, удаляет и выводит первый
        #   элемент стека( 35 == 35)
        self.assertEqual(test1.pop_head(), 35)

        #   Проверка метода, удаляет и выводит первый
        #   элемент стека( 52 == 52)
        self.assertEqual(test1.pop_head(), 52)
        test1.pop()

        #   Проверка стека на None, стек пустой
        self.assertEqual(test1.pop_head(), None)
        self.assertIsNone(test1.pop_head())

    def tets_peak_head(self):

        test2 = Stack.Stack()
        test2.push(75)
        test2.push(56)
        test2.push(12)
        test2.push(35)

        #   Проверка метода, выводит первый
        #   элемент стека( 75 == 75)
        self.assertEqual(test2.peak_head(), 75)

        #  Удаляем первый элемент стека
        test2.pop_head()

        #   Проверка метода, выводит первый
        #   элемент стека( 56 == 56)
        self.assertEqual(test2.peak_head(), 56)

        #   Удаляем все элементы стека
        while test2.size() > 0:
            test2.pop()

        #   Проверка стека на None, стек пустой
        self.assertEqual(test2.peak_head(), None)
        self.assertIsNone(test2.peak_head())

    def test_balance_brackets(self):
        # данные для проверки корректные
        test1 = Stack.balance_brackets('()()')

        # данные для проверки не корректные
        test2 = Stack.balance_brackets(')()(')
        # данные для проверки корректные
        test3 = Stack.balance_brackets('(()(()()))')
        # данные для проверки не корректные, кол-во скобок разное
        test4 = Stack.balance_brackets('(()))')

        self.assertTrue(test1)
        self.assertFalse(test2)
        self.assertTrue(test3)
        self.assertFalse(test4)

    def test_expression_solution(self):
        test1 = []
        test2 = [ 1, '-',1]
        test3 = [1, '+', 1]
        test4 = [1, 1]
        test5 = [1, 1, '+', 1, '+', 5, '*']

        self.assertFalse(Stack.expression_solution(test1))
        self.assertFalse(Stack.expression_solution(test2))
        self.assertFalse(Stack.expression_solution(test3))
        self.assertFalse(Stack.expression_solution(test4))
        self.assertTrue(Stack.expression_solution(test5))
        self.assertEqual(Stack.expression_solution(test5), 15)