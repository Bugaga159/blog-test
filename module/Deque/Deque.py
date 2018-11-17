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


deq = Deque()
deq.addFront("f1")
deq.addTail("t1")
deq.addFront("f2")
deq.addTail("t2")
deq.addTail("t3")

print(deq.queue)