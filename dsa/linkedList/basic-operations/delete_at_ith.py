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


def delete_at_i(head, i):

    if i < 0 or i >= length(head):
        return head

    cur = head

    if i == 0:
        head = cur.next
        return head

    for _ in range(i-1):
        cur = cur.next

    cur.next = cur.next.next
    return head


head = takeinput()
head = delete_at_i(head, 1)
printLinkedList(head)

