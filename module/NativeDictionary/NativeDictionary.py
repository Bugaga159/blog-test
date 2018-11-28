from module.HashTable.HashTable import HashTable

class NativeDictionary(HashTable):
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.dictionary = [None] * self.size


    def put(self, key, value):
        if self.find(key) is not None:
          self.dictionary[self.find(key)] = value
        else:
          index = self.seek_slot(key)
          if index is not None:
              self.slots[index] = key
              self.dictionary[index] = value
          else:
              return None

    def is_key(self, key):
        index = self.find(key)
        if index is not None:
            return True
        else:
            return None


    def get(self, key):
        index = self.find(key)
        if index is not None:
            return self.dictionary[index]
        else:
            return None

  
