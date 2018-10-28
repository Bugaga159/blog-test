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
    rot = Queue()
    rot.items = item
    while n:
        rot.enqueue(rot.dequeue())
        n -= 1
    return rot.items







