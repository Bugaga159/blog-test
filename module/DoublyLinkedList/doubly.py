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

    # Удаление узла по значение, если нужно удалить во всех узлах значение, то all=TRUE
    def delete(self, val):
        if self.head is None:
            return True
        elif self.head.value == val:
            if self.head == self.tail:
                self.tail = None
                self.head = None
            else:
                self.head = self.head.next
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
                    break
                else:
                    node = node.next

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
            self.tail = self.head
            return True
        else:
            node = self.head
            while node is not None:
                if node.value == afterNode.value:
                    if node == self.tail:
                        node.next = newNode
                        node.next.prev = node
                        self.tail = node.next
                    else:
                        new_node = newNode
                        new_node.next = node.next
                        new_node.next.prev = new_node
                        new_node.prev = node
                        node.next = new_node
                    return True
                node = node.next
            return False

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


