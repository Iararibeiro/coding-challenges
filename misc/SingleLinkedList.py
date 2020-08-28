class SingleListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None

    def setNext(self, node):
        self.next = node

    def getNext(self):
    	return self.next

    def getValue(self):
        return self.value
