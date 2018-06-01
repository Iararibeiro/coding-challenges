from SingleLinkedList import SingleListNode

def solution(head, partition):
    #less, greater, less_head, greater_head = None
    less = None
    less_head = None
    greater = None
    greater_head = None

def printList(head):
	result = "["
	node = head
	while node:
		result += str(node.getValue()) + ","
		node = node.getNext()

	result = result[:-1]
	result += "]"
	return result

head = SingleListNode(3)
element1 = SingleListNode(5)
element2 = SingleListNode(8)
element3 = SingleListNode(5)
element4 = SingleListNode(10)
element5 = SingleListNode(2)
element6 = SingleListNode(1)

head.setNext(element1)
element1.setNext(element2)
element2.setNext(element3)
element3.setNext(element4)
element4.setNext(element5)
element5.setNext(element6)

#print(printList(head))
solution(head, 5)
#print(printList(solution(head, 5)))
