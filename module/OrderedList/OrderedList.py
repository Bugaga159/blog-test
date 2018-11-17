class Node:
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



