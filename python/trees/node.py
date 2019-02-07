class Node:

	def __init__(self, data):
        self._data = data
        self._children = []

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, obj):
        self._children = obj

    def add_children(self, child):
        self._children.append(child)

    def print(self):
        return (self._data + ", children: " + self._children)
