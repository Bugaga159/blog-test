from module.Stack import Stack

class QueuesThroughTheStack:
    def __init__(self):
        self.item = Stack.Stack()
        self.S2 = Stack.Stack()

    def enqueue(self, item):
        if self.item.size() != 0:
            while self.item.size():
                self.S2.push(self.item.pop())
            self.S2.push(item)
            while self.S2.size():
                self.item.push(self.S2.pop())
        else:
           self.item.push(item)

    def dequeue(self):
        return self.item.pop()

    def size(self):
        return self.item.size()

test = QueuesThroughTheStack()
test.enqueue(124)
test.enqueue(4)
test.enqueue(64)
test.enqueue(8)
res = test.item.stack
print(res)