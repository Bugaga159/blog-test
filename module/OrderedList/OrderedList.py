class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

class OrderedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.sortArrs = None
        self.array = []



    def sortArr(self, lev=0):
        node = self.head
        self.array = []
        while node is not None:
            self.array.append(node.value)
            node = node.next
        if lev == 0:
            self.sortArrs = 'ASC'
        elif lev == 1:
            self.sortArrs = 'DESC'
            res = []
            for i in self.array:
                res.insert(0, i)
            self.array = res




    # Метод сравнения двух значений
    def comparison(self, val1, val2):
        if int(val1) > int(val2):
          return True
        else:
          return False

    # Добавление в список
    def add_in_tail(self, item):

        if self.head  is None:
          self.head = self.tail = item
        else:
          node = self.head
          if self.comparison(node.value, item.value):
            prev = item
            prev.next = node
            self.head = prev
          elif node.next is None:
            node.next = item
            self.tail = item
          else:
            while node.next is not None:
              if self.comparison(node.next.value, item.value):
                prev = item
                prev.next = node.next
                node.next = prev
                break
              else:
                node = node.next
                if node.next is None:
                  node.next = item
                  self.tail = item
                  break
    # метод удаления одного узла по его значению
    def remove(self, val):
          if self.head == None:
              return None
          elif self.head.value == val:
              self.head = self.head.next
          else:
              node = self.head
              while node.next is not None:
                  if node.next.value == val:
                      if node.next == self.tail:
                          self.tail = node
                          node.next = None
                          break
                      node.next = node.next.next
                      break
                  node = node.next

    def search(self, val):
        node = self.head
        while node is not None:
            if self.comparison(node.value, val):
                return False
            if node.value == val:
                return True
            node = node.next
        return None



class СomparisonStrings(OrderedList):
    def add_in_tail(self, item):
        prev = item
        prev.value = item.value.strip()
        super().add_in_tail(prev)

    # Сравнение лексикографическое
    def comparison(self, val1, val2):
        if val1 > val2:
          return True
        else:
          return False

