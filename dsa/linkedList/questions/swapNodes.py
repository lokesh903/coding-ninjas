
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def swapNodes(head, i, j):
    cur = head
    index = 0
    node1, node2, preNode1, preNode2 = None, None,None ,None
    pre = None
    while cur:
        if index == i:
            node1 = cur
            preNode1 = pre
        if index == j:
            node2 = cur
            preNode2 = pre
        index+=1
        pre = cur
        cur = cur.next
        
    if node1 is None or node2 is None:
        return head
    

    if preNode1:
        preNode1.next = node2
    if preNode2:
        preNode2.next = node1
    
    
    tempNode1Next = node1.next
    node1.next = node2.next
    node2.next = tempNode1Next
    
    if node1 == head:
        head = node2
    elif node2 == head:
        head = node1
    
            
    return head
    
    

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
i,j = list(map(int,input().split()))
newHead = swapNodes(head, i, j)

printLinkedList(newHead)