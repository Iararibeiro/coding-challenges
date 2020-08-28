from SingleLinkedList import SingleListNode

def addTwoNumbers(l1, l2):
    return sumLists(l1, l2, 0)

def sumLists(l1, l2, c):
    val = l1.val + l2.val + c
    c = val // 10
    ret = SingleListNode(val % 10 )

    if (l1.next != None or l2.next != None or c != 0):
        if l1.next == None:
            l1.next = SingleListNode(0)
        if l2.next == None:
            l2.next = SingleListNode(0)
        ret.next = sumLists(l1.next,l2.next,c)
    return ret

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
