from com.cabbage.basic.data_structure.collection.node import Node


class LinkedBag(object):
    """A linked-base bag implementation"""

    # Constructor
    def __init__(self, source=None):
        """Set the initial state of self, which include the contents of source collection , if this present."""
        self._item = None
        self._size = 0
        self.addAll(source)

    def isEmpty(self):
        """return True if len(self) == 0, or False otherwise"""
        return self.__len__() == 0

    def __len__(self):
        """return thr number of items in self"""
        return self._size

    def __str__(self):
        """Returns the string representation of selef."""
        return "{" + ",".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of self"""
        cursor = self._item
        while cursor is not None:
            yield cursor.data
            cursor = cursor.next

    def __add__(self, other):
        """Returns a new bag containing the contents of self."""
        result = LinkedBag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Return True if self equals other , or False otherwise"""
        if self is other: return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        for i in self:      # 当python识别到in运算符时 它会运行集合中的_contains_方法
            if i not in other:
                return False
        return True

    def clear(self):
        """Makes self become empty."""
        self._item = None
        self._size = 0

    def add(self, item):
        """Adds item to self"""
        # Check array memory here and increase it if necessary
        self._item = Node(item, self._item)

    def addAll(self, source):
        """Adds source collection to self"""
        if source:
            for i in source:
                self.add(i)

    def remove(self, item):
        """Predication：item is in self.
        Raise: KeyError if item is not in self.
        PostCondition：item is removed from self."""
        # Check precondition and raise if necessary
        if item not in self:
            raise KeyError(str(item) + " not in bag")
        # Search for index of target item
        target_index = 0
        for i in self:
            if i == item:
                break
            target_index += 1

        # Shift items to the left of target up on position
        for i in range(target_index, len(self)-1):
            self._item[i] = self._item[i+1]

        # Decrement logical size
        self._size -= 1

if __name__ == '__main__':
    lyst = [2013, 61, 1973]
    b1 = LinkedBag(lyst)
    print(b1)