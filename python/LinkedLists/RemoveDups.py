from SingleLinkedList import SingleListNode

def solution(head):
	node = head
	while node is not None:
		leaf = node.getNext()
		if leaf is not None:
			if node.getValue() == leaf.getValue():
				node.setNext(leaf.getNext())
		node = node.getNext()

def printList(head):
	result = "["
	node = head
	while node:
		result += str(node.getValue()) + ","
		node = node.getNext()

	result = result[:-1]
	result += "]"
	return result

head = SingleListNode(0)
element1 = SingleListNode(1)
element2 = SingleListNode(1)
element3 = SingleListNode(2)
head.setNext(element1)
element1.setNext(element2)
element2.setNext(element3)

print(printList(head))
solution(head)
print(printList(head))
