"""
树的链表结构实现
"""

from com.cabbage.basic.data_structure.collection.array_stack import ArrayStack

class LinkedBST(object):

    def __init__(self):
        self._root = None

    """搜索"""
    def find(self, item):

        def recurse(node):
            if node is None:
                return None
            elif node.data == item:
                return node.data
            if item<node.data:
                return recurse(node.left)
            else: return recurse(node.right)

        return recurse(self._root)

    """中序遍历"""
    def inorder(self):
        lst = list()

        def recurse(node):
            if node is not None:
                recurse(node.left)
                lst.append(node.data)
                recurse(node.right)
        recurse(self._root)
        return iter(lst)

    """前序遍历"""
    def __iter__(self):
        stack = ArrayStack()
