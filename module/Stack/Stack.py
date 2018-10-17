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
