"""
栈 的链表结构实现
"""

from com.cabbage.basic.data_structure.collection.node import Node
from com.cabbage.basic.data_structure.collection.abstract_stack import AbstractStack


class LinkedStack(AbstractStack):

    def __init__(self):
        self.items = None
        AbstractStack.__init__(self)

    def __iter__(self):
        def visit_nodes(node):
            if not node is None:
                visit_nodes(node.next)
                tmp_list.append(node)
        tmp_list = list()
        visit_nodes(self.items)
        return iter(tmp_list)

    def peek(self):
        return self.items.data

    def clear(self):
        self.items = None

    def push(self, item):
        self.items = Node(item, self.items)

    def is_empty(self):
        return self.items is None

    def pop(self):
        if self.is_empty():
            raise KeyError("This stack is empty")
        old_item = self.items.data
        self.items = self.items.next
        return old_item

    def __str__(self):
        def visit_nodes(node):
            if not node is None:
                visit_nodes(node.next)
                tmp_list.append(node.data)
        tmp_list = list()
        visit_nodes(self.items)
        return str(tmp_list)


def test(stack_type):
    s = stack_type()
    print("Empty:", s.is_empty())
    print("push 1-10")
    for i in range(10):
        s.push(i+1)
    print("peeking:",s.peek())
    print("items:", s)
    print("Items (bottom to top):", s.pop())
    print("Empty:",s.is_empty())


if __name__ == "__main__":
    test(LinkedStack)