class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# функция, которая "вращает" очередь по кругу на N элементов.
def rotation(item, n=0):
    while n:
        item.insert(0, item.pop())
        n -= 1
    return item






