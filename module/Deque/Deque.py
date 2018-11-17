class Deque:
    def __init__(self):
        self.queue = []

    def addFront(self, item):
        self.queue.append(item)

    def addTail(self, item):
        self.queue.insert(0,item)

    def removeFront(self):
        return self.queue.pop()

    def removeTail(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

# Проверяет строку, является ли некоторая строка палиндромом
def palindrome(strCheck):
    n = Deque()
    n.queue = list(strCheck)
    while n.size() != 0:
        if n.removeFront() == n.removeTail():
            continue
        else:
            return False
    return True

