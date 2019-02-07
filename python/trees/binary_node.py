class BNode:

	def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None

    @property
    def value(self):
        return self._data

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, obj):
        self._left = obj

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, obj):
        self._right = obj


    def print(self):
        return ("Node: " + self._data + ", left leaf: " + self._left + ", right leaf:" + self._right)
