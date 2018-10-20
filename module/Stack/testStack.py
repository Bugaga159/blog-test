import unittest
from . import Stack

class testStackClass( unittest.TestCase):
    def test_pop_head(self):
        test1 = Stack.Stack()
        test1.push(35)
        test1.push(52)
        test1.push(7)

        '''
            Тест проверки на вывод первого элемента 
            и удаляется из Стека,
            первый элемент Стека равен 35.
        '''
        self.assertEqual(test1.pop_head(), 35)

        '''
            Тест проверки на вывод первого элемента 
            и удаляется из Стека,
            первый элемент Стека равен 52.
        '''
        self.assertEqual(test1.pop_head(), 52)


