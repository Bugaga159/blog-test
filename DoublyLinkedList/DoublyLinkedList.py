class Node2:
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

    # метод удаления одного узла по его значению
    def remove(self, val):
        if self.head == None:
            return None
        elif self.head.value == val:
            self.head = self.head.next
            self.head.prev = None
        else:
            node = self.head
            while node is not None:
                if node.next.value == val:
                    if node.next.next != None:
                        node.next = node.next.next
                        node.next.prev = node
                    else:
                        node.next = None
                    break
                node = node.next
    # метод вставки узла после заданного узла.
    def add_val_after(self, val1, val2):
        node = self.head
        if self.head == None:
            return None
        else:
            while node is not None:
                if node.value == val1:
                    prev = Node2(val2)
                    prev.next = node.next
                    node.next = prev
                    node.next.prev = node
                    break
                node = node.next

    # метод вставки узла самым первым элементом.
    def add_first(self, val):
        if self.head == None:
            self.head = Node2(val)
            item.prev = None
            item.next = None
        else:
            new_node = Node2(val)
            new_node.next = self.head
            new_node.prev = None
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node

# Показать связанный список
    def show(self):
        node = self.head
        while node != None:
            if node.prev == None:
                print('None')
            else:
                print(node.prev.value)
            print(node.value)
            if node.next == None:
                print('None')
            else:
                print(node.next.value)
            print('*' * 9)
            node = node.next


list2 = LinkedList2()
list2.add_in_tail(Node2(12))
list2.add_in_tail(Node2(14))
list2.add_in_tail(Node2(36))
list2.add_in_tail(Node2(48))
list2.remove(36)
list2.add_val_after(14,22)
list2.add_first(64)
list2.show()

