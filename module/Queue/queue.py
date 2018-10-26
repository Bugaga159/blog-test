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
def rotation(queue, n=0):
    while n:
        queue.insert(0, queue.pop())
        n -= 1
    return queue

