class Node:
    def __init__(self,data) :
        self.data = data
        self.next = None
    
def getMid(head):
    
    slow, fast = head, head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

def mergeLL(h1,h2):
    
    
    demoNode = Node(-1)
    p1,p2 = h1,h2
    cur = demoNode
    while p1 and p2:
        if p1.data > p2.data:
            cur.next = p2
            p2 = p2.next
        else:
            cur.next = p1
            p1 = p1.next
        cur = cur.next
    if p1:
        cur.next = p1
    if p2:
        cur.next = p2
        
    return demoNode.next

def mergeSort(head):
    
    if head is None or head.next is None:
        return head
    
    mid = getMid(head)
    part1 = head
    part2 = mid.next
    mid.next = None
    
    h1 = mergeSort(part1)
    h2 = mergeSort(part2)
    
    newHead = mergeLL(h1,h2)

    return newHead
    
    # get the mid
    # create part1
    # create part2
    # break the mid.next
    
    # sort p1
    # sort p2
    # merge p1, p2
    # return newHead
    
    
    
# 1 2 3 4 -1











def takeinput():
    intlist = list(map(int, input().split()))

    cur = Node(intlist[0])
    head = cur

    for i in range(1, len(intlist)):
        newNode = Node(intlist[i])
        cur.next = newNode
        cur = newNode

    return head


def printLinkedList(head):

    cur = head
    while cur is not None:
        print(cur.data, end=" ")
        cur = cur.next

head = takeinput()
newHead = mergeSort(head)

printLinkedList(newHead)