class SingleListNode(object):

    def __init__(self, value):
        self.val = value
        self.next = None

    def setNext(self, node):
        self.next = node

    def getNext(self):
    	return self.next

    def getVal(self):
        return self.val
