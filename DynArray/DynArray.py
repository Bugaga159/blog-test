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
        for u in range(self.count):
            if u == i:
                new_array.append(itm)
                new_array.append(self.array[u])
            elif u > i:
                new_array.append(self.array[u])
            else:
                new_array.append(self.array[u])
        self.count += 1
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        for u in range(self.count):
            self.array[u] = new_array[u]


    def delete(self, i):
        new_array = []
        for u in range(self.count):
            if u == i:
                continue
            else:
                new_array.append(self.array[u])
        self.count -= 1
        for u in range(self.count):
            self.array[u] = new_array[u]

        if (self.capacity / 2) > self.count and self.capacity > 16:
            if self.count == self.capacity:
                self.resize(2 * self.capacity)
            else:
                self.capacity = int(self.capacity / 2)



