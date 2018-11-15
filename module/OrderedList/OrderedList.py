class Node2:
    def __init__(self, v):
        self.value = v
        self.next = None

class OrderedList:
  def __init__(self,s = 0):
    self.head = None
    self.tail = None
    self.sort = None

    if s == 0:
      self.sort = 'ASC'
    elif s == 1:
      self.sort = 'DESC'
  # Метод сравнения двух значений
  def comparison(self, val1, val2):
    if val1 > val2:
      return True
    elif val1 <= val2:
      return False
        
  # Добавление в список
  def add_in_tail(self, item):
    if self.head is None:
      self.head = self.tail = item
    else:
      node = self.head
      while node is not None:
        if self.comparison(node.value, item.value):
          prev = item
          prev.next = self.head
          self.head = prev
          break
        elif node.next is None:
          node.next = item
          self.tail = item
          break
        node = node.next


  # Удалить заданное значение в связанном списке все
  def removeAllVal(self, val):
    if self.head.value == val:
      self.head = self.head.next
    if self.head == None:
      return None
    else:
      node = self.head
      while node.next is not None:
        if node.next.value == val:
          if self.tail == node.next:
            self.tail == node.next.next
          node.next = node.next.next
        else:
          node = node.next



    
test = OrderedList()
test.add_in_tail(Node2(2))
test.add_in_tail(Node2(1))
test.add_in_tail(Node2(3))

print(test.head.next.value)


