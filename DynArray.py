import ctypes
class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        new_array = []
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        for u in range(self.count):
            if u == i:
                new_array.append(itm)
                new_array.append(self.array[u])
            elif u > i:
                new_array.append(self.array[u])
            else:
                new_array.append(self.array[u])
        self.count +=1
        self.array = new_array

da = DynArray()
da.append(23)
da.append(35)
da.append(77)
da.append(6)
da.append(48)
da.insert(1, 57)
for i in range(len(da)):
    print(da[i])
