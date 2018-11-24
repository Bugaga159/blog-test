class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        
    # Вычисляет индекс слота
    def hash_fun(self, value):
      key = 0
      byteArr =  list(map(ord, str(value)))
      for i in range(len(byteArr)):
        key += byteArr[i]
      key = key % self.size
      return key
      
    # метод  поиска слота, значению сперва рассчитывает 
    # индекс хэш-функцией, а затем отыскивает подходящий 
    # слот для него с учётом коллизий, или возвращает None
    def seek_slot(self, value):
      index = self.hash_fun(value)
      print(index)
      
      for i in range(self.size):
        if self.slots[index] is None:
          self.slots[index] = value
          return True
        else:
          index += self.step
          i += self.step
        if i > self.size:
          return None
      return None
