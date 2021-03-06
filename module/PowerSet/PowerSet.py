from module.HashTable.HashTable import HashTable

class PowerSet(HashTable):

    # добавление
    def put(self, value):
        k = self.find(value)
        if k is None:
            index = self.seek_slot(value)
            if index is not None:
                self.slots[index] = value
            else:
                return None
        else:
            return None

    #   удаление элемента из множества
    def remove(self, value):
        index = self.find(value)
        if index is not None:
            self.slots[index] = None
        else:
            return None


    #   в качестве параметра выступает другое множество, 
    #   а возвращается пересечение этих множеств
    def intersection(self, value):
        common = []
        for i in value:
            if i is not None:
                res = self.find(i)
                if res is not None:
                    common.append(self.slots[res])

        return common
    
    #   в качестве параметра выступает другое множество, 
    #   а возвращается объединение этих множеств
    def union(self, val):
        sumSet = []
        for i in val:
            if i is not None:
                res = self.find(i)
                if res is None:
                    sumSet.append(i)
        for k in self.slots:
            if k is not None:
                sumSet.append(k)
        return sumSet



    #   в качестве параметра выступает другое множество, 
    #   а возвращается подмножество текущего множества из
    #   таких элементов, которые не входят в множество-параметр;
    def difference(self, value):
        common = []
        for i in value:
            if i is not None:
                res = self.find(i)
                if res is None:
                    common.append(i)
        return common

    #   в качестве параметра выступает другое множество, 
    #   и проверяется, входят ли все его элементы в текущее множество
    def issubset(self, value):
        for i in value:
            if i is not None:
                res = self.find(i)
                if res is None:
                    return False
        return True
