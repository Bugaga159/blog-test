class NativeDictionary:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.dictionary = {}
        
    # Вычисляет индекс слота
    def hash_fun(self, value):
        return sum(list(map(ord, str(value)))) % self.size
      
    # метод  поиска слота, значению сперва рассчитывает 
    # индекс хэш-функцией, а затем отыскивает подходящий 
    # слот для него с учётом коллизий, или возвращает None
    def seek_slot(self, value):
        index = self.hash_fun(value)
        for i in range(self.size):
            if index > self.size-1:
                return None
            if self.slots[index] is None:
                return index
            else:
                if index == i:
                    index += self.step
        return None

    # помещает значение value в слот,
    # вычисляемый с помощью функции поиска
    def put(self, key, value):
        index = self.seek_slot(key)
        if index != None:
            self.slots.insert(index, key)
            self.dictionary[key] = value
        else:
            return None
    # проверяет, имеется ли в слотах указанное значение, 
    # и возвращает либо слот, либо None.
    def is_key(self, key):
        index = self.hash_fun(key)
        if self.slots[index] == key:
            return key
        else:
            for i in range(self.size):
                if self.slots[i] == key:
                    return key
        return None
    def get(self, key):
        index = self.is_key(key)
        if index != None:
            return self.dictionary[index]
        else:
          return None
