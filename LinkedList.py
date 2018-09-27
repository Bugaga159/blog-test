class Node:
    def __init__(self, v=None):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Добавить новый узел
    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    # Распечатать весь связанный список
    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    # Найти значение в связанном списке
    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    # Удалить значение в связанном списке
    def remove(self, val):
        if self.head == None:
            return None
        elif self.head.value == val:
            self.head = self.head.next
        else:
            node = self.head
            while node.next is not None:
                if node.next.value == val:
                    if self.tail == node.next:
                        self.tail == node.next.next
                    node.next = node.next.next
                    break
                node = node.next

    # Удалить заданное значение в связанном списке все
    def removeAllVal(self, val):
        if self.head == None:
            return None
        elif self.head.value == val:
            self.head = self.head.next
        else:
            node = self.head
            while node.next is not None:
                if node.next.value == val:
                    if self.tail == node.next:
                        self.tail == node.next.next
                    node.next = prev = node.next.next
                else:
                    node = node.next

    # Очистить список
    def clearAll(self):
        self.head = None
        self.tail = None

    # Найти заданое значение все в связанном списке
    def findVal(self, val):
        if self.head == None:
            return None
        else:
            res = []
            node = self.head
            num = 1
            while node is not None:
                num += 1
                if node.value == val:
                    res.append([node.value, num])
                node = node.next
            return res

    # Длина списка
    def lengthList(self):
        node = self.head
        len = 1
        while node.next != None:
            len += 1
            node = node.next
        return len

    # Вставки узла после заданного узла
    def add_val_after(self, val1, val2):
        node = self.head
        if self.head == None:
            return None
        else:
            while node is not None:
                if node.value == val1:
                    prev = Node(val2)
                    prev.next = node.next
                    node.next = prev
                    break
                node = node.next


s_list = LinkedList()
s_list.add_in_tail(Node(35))
s_list.add_in_tail(Node(54))
s_list.add_in_tail(Node(2))
s_list.add_in_tail(Node(24))
s_list.add_in_tail(Node(48))

s_list.add_val_after(24,45)

s_list.print_all_nodes()
