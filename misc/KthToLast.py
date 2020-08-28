from SingleLinkedList import SingleListNode

def solution(head, k):
    if head is None:
        return 0;

    index = solution(head.getNext(), k) + 1;
    if index == k:
        print(head.getValue())
        print(str(index) + "th to last element is " + str(head.getValue()))
    return index

head = SingleListNode(0)
element1 = SingleListNode(1)
element2 = SingleListNode(2)
element3 = SingleListNode(3)
element4 = SingleListNode(4)
element5 = SingleListNode(5)

head.setNext(element1)
element1.setNext(element2)
element2.setNext(element3)
element3.setNext(element4)
element4.setNext(element5)

solution(head, 3)
