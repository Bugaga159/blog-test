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

    def return_all_nodes(self):
        node = self.head
        arrNodes = []
        while node is not None:
            arrNodes.append(node.value)
            node = node.next
        return arrNodes

    # Найти значение в связанном списке
    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    # Удаление узла по значение, если нужно удалить во всех узлах значение, то all=TRUE
    def delete(self, val, all=False):
        if self.head == None:
            return True
        elif self.head.value == val:
            if self.head == self.tail:
                self.tail = None
            if all:
                self.head = self.head.next
                self.delete(val, True)
            else:
                self.head = self.head.next

        else:
            node = self.head
            while node.next is not None:
                if node.next.value == val:
                    if node.next == self.tail:
                        self.tail = node
                        node.next = None
                        break
                    elif all == False:
                        node.next = node.next.next
                        break
                    else:
                        node.next = node.next.next
                else:
                    node = node.next



    # Очистить список
    def clean(self):
        self.head = None
        self.tail = None

    # Найти заданое значение все в связанном списке
    def find_all(self, val):
        if self.head == None:
            return []
        else:
            res = []
            node = self.head
            while node is not None:
                if node.value == val:
                    res.append(node)
                node = node.next
            return res


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
        node = self.head
        if self.head == None:
            self.add_in_tail(Node(newNode))
            return True
        else:
            while node is not None:
                if node.value == afterNode:
                    prev = Node(newNode)
                    prev.next = node.next
                    node.next = prev
                    return True
                node = node.next
            return False

"""
Функция Comparison(),функцию, которая получает на вход два связанных списка,
 состоящие из целых значений, и если их длины равны, возвращает список,
 каждый элемент которого равен сумме соответствующих элементов входных списков.
"""


def Comparison(link1, link2):
    length1 = link1.len()
    length2 = link2.len()
    list_sum = LinkedList()
    list_link1 = link1.head
    list_link2 = link2.head

    if length1 == length2:
        while list_link1 is not None and list_link2 is not None:
            res = list_link1.value + list_link2.value
            list_sum.add_in_tail(Node(res))
            list_link1 = list_link1.next
            list_link2 = list_link2.next
    return list_sum

