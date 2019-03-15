class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    # Найти значение в связанном списке
    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    # Найти все узлы по значению
    def find_all(self, val):
        quantityNode = []
        node = self.head
        while node is not None:
            if node.value == val:
                quantityNode.append(node)
            node = node.next
        return quantityNode

    # Удаление узла по значение
    def delete(self, val):
        if self.head is None:
            return None
        elif self.head.value == val:
            if self.head == self.tail:
                self.tail = None
                self.head = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return True
        else:
            node = self.head
            while node.next is not None:
                if node.next.value == val:
                    if node.next == self.tail:
                        self.tail = node
                        node.next = None
                    else:
                        node.next = node.next.next
                        node.next.prev = node
                    return True
                else:
                    node = node.next
            return None

    # Очистить список
    def clean(self):
        self.head = None
        self.tail = None

    # Длина списка
    def len(self):
        node = self.head
        res = 0
        while node is not None:
            res += 1
            node = node.next
        return res

    # Вставки узла после заданного узла
    def insert(self, afterNode, newNode):
        if self.head is None:
            self.head = newNode
            newNode.prev = None
            newNode.next = None
            self.tail = newNode
        else:
            resultFound = self.find(afterNode.value)   
            if resultFound is not None:
                prevNode = newNode
                prevNode.next = resultFound.next
                resultFound.next = prevNode
                if resultFound == self.tail:
                    self.tail = resultFound.next
            else:
            	  self.add_in_tail(newNode)

    def add_in_head(self, newNode):
        if self.head is None:
            self.head = newNode
            self.tail = self.head
        else:
            new_node = newNode
            self.head.prev = new_node
            new_node.next = self.head
            if self.tail == self.head:
                self.tail = self.head
            new_node.prev = None
            self.head = new_node


