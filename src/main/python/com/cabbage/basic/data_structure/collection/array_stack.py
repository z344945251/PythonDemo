
"""
栈 的数组实现
"""

from com.cabbage.basic.data_structure.collection.abstract_stack import AbstractStack


class ArrayStack(AbstractStack):

    def __init__(self):
        self.items = list()
        AbstractStack.__init__(self)

    def __iter__(self):
        cursor = 0
        while cursor < len(self.items):
            yield self.items[cursor]
            cursor += 1

    def peek(self):
        return self.items[len(self) - 1]

    def clear(self):
        self.items = list()

    def push(self, item):
        self.items[len(self)] = item

    def pop(self):
        item = self.items[len(self)-1]
        self.items.remove(len(self)-1)
        return item
