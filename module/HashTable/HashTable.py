class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        
    # Вычисляет индекс слота
    def hash_fun(self, value):
        key = 0
        byteArr = list(map(ord, str(value)))
        for i in range(len(byteArr)):
            key += byteArr[i]
        key = key % self.size
        return key
      
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
    def put(self, value):
        index = self.seek_slot(value)
        if index != None:
            self.slots.insert(index, value)
        else:
            return None

    def find(self, value):
        for i in range(self.size):
            if self.slots[i] == value:
                return i
        return None


