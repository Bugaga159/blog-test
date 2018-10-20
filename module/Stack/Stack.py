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

print(balance_brackets('(()((())()))'))


