from SingleLinkedList import SingleListNode

def addTwoNumbers(l1, l2):
    return sumLists(l1, l2, 0)

def sumLists(l1, l2, carryOn):
    if not l1 and not l2 and carryOn == 0: return None

    value = carryOn
    result = SingleListNode(0)

    if l1.val > 0:
        value += l1.val
    if l2.val > 0:
        value += l2.val

    result.val = value % 10

    if l1.val > 0 or l2.val > 0:
        if value >= 10:
            nextValue = sumLists(l1.next, l2.next, 1)
            result.next = nextValue
        else:
            nextValue = sumLists(l1.next, l2.next, 0)
            result.next = nextValue

    return result

def printList(head):
	result = "["
	node = head
	while node:
		result += str(node.getVal()) + ","
		node = node.getNext()

	result = result[:-1]
	result += "]"
	return result

l1 = SingleListNode(1)
element1 = SingleListNode(1)
element2 = SingleListNode(6)
#l1.setNext(element1)
#element1.setNext(element2)

l2 = SingleListNode(9)
element3 = SingleListNode(9)
element4 = SingleListNode(2)
l2.setNext(element3)
#element3.setNext(element4)

print(printList(addTwoNumbers(l1,l2)))
