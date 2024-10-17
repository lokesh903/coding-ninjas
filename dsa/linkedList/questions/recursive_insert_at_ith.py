class Node:
    def __init__(self, data) -> None:
        self.next = None
        self.data = data


def takeinput():
    intlist = list(map(int, input().split()))

    cur = Node(intlist[0])
    head = cur

    for i in range(1, len(intlist)):
        newNode = Node(intlist[i])
        temp = cur
        temp.next = newNode
        cur = newNode

    return head


def printLinkedList(head):
    cur = head
    while cur is not None:
        print(cur.data, end=" ")
        cur = cur.next


def length(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next

    return count


def recursive_insert_at_i(head, i, val):

    if i < 0:
        return head

    if i == 0:
        newNode = Node(val)
        newNode.next = head
        return newNode
    if head is None:
        return head

    head.next = recursive_insert_at_i(head.next, i - 1, val)
    return head


head = takeinput()
head = recursive_insert_at_i(head, 4, 0)
printLinkedList(head)
