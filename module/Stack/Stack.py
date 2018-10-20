class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def push(self, value):
        return self.stack.append(value)

    def peak(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)
    
    #Удаляет 1 элемент стека
    def pop_head(self):
      if len(self.stack) == 0:
            return None
      return self.stack.pop(0)
      
    #Возвращает 1 элемент стека
    def peak_head(self):
      if len(self.stack) == 0:
            return None
      return self.stack[0]


def balance_brackets(x):
    checkArr = Stack()
    if (len(x) % 2) != 0:       #Проверка на четное количество элементов
        return False
    for i in range(len(x)):
        if checkArr.size() == 0 and x[i] == '(':
            checkArr.push(x[i])
        elif checkArr.peak_head() != x[i]:
            checkArr.pop()
        else:
            checkArr.push(x[i])
    if checkArr.size() == 0:
        return True
    else:
        return False

# функция выполняет операции + и * , с элементами в Стеке
def expression_solution(x):
    S1 = Stack()
    S2 = Stack()
    if x is None:
        return None
    for i in range(len(x)):
        S1.push(x[i])
    if '+' in x and '*' in x:
        while S1.size() > 0:
            if S1.stack[0] == '+':
                S2.push(S2.pop() + S2.pop())
                S1.pop_head()
            elif S1.stack[0] == '*':
                S2.push(S2.pop() * S2.pop())
                S1.pop_head()
            elif S1.stack[0] == '=':
                return S2.stack[0]
            else:
                S2.push(S1.pop_head())
    else:
        return False
    return S2.stack[0]

num1 = '()(()())'
print(balance_brackets(num1))

