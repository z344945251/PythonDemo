class BagInterface(object):
    def __init__(self):
        pass

    def isEmpty(self):
        return True

    def __len__(self):
        return 0

    def __str__(self):
        return ""

    def __iter__(self):
        return None

    def __add__(self, other):
        return None

    def __eq__(self, other):
        return False

    def clear(self):
        pass

    def add(self, item):
        pass

    def addAll(self, source):
        pass

    def remove(self, item):
        pass
