
class Array(object):

    DEFAULT_CAPACITY = 5

    def __init__(self, capacity=DEFAULT_CAPACITY, fill_value=None):
        self.items = list()
        self._size = 0
        for count in range(capacity):
            self.items.append(fill_value)

    def __str__(self):
        return str(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, new_item):
        self.items[index] = new_item

    def __len__(self):
        return self.items.__len__()

    def __iter__(self):
        return iter(self.items)


if __name__ == "__main__":
    arr = Array(10)
    print(arr)
    print(arr[0])
