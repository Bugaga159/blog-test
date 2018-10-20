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
    x1 = x2 = 0
    if (len(x) % 2) != 0:       #Проверка на четное количество элементов
        return False
    for i in range(len(x)):     #Для проверки на равное количество скобок откр/закр
        if x[i] == '(':
            x1 +=1
        elif x[i] == ')':
            x2 +=1
    if x1 == x2:
        for i in range(len(x)):
            if checkArr.size() == 0 and x[i] == '(':
                checkArr.push(x[i])
            elif checkArr.peak_head() != x[i]:
                checkArr.pop()
            else:
                checkArr.push(x[i])

    else:
        return False
    if checkArr.size() == 0:
        return True
    else:
        return False

# функция выполняет операции + и * , с элементами в Стеке
def expression_solution(x):
    S1 = Stack()
    S2 = Stack()
    for i in range(len(x)):
        S1.push(x[i])
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
    return S2.stack[0]

num1 = [ 1, 2, '+', 3, '*' ]
num2 = [8, 2, '+', 5, '*', 9, '+', '=']
print('1 2 + 3 * =>',expression_solution(num1))
print('8 2 + 5 * 9 + = =>',expression_solution(num2))

