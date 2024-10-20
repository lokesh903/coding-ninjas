class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
        
def evenAfterOdd(head):
    
    # four pointer odd head,tail and even head,tail
    oh,ot,eh,et = None,None,None,None
    if head is None or head.next is None:
        return head
    
    cur = head
    
    # make 2 ll using 4 pointers one for odd one for even 
    while cur:
        
        if cur.data % 2 == 0:
            if eh is None:
                eh = cur
                et = cur
            else:
                et.next = cur
                et = et.next
        else:
            if oh is None:
                oh = cur
                ot = cur
            else:
                ot.next = cur
                ot = ot.next
        cur = cur.next
        
    # if all  nodes are even
    if oh is None:
        return head
    # if all  nodes are odd
    if eh is None:
        return head
    ot.next = eh
    et.next = None
    
    return oh
                 
    
    
    
    

    












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
newHead = evenAfterOdd(head)

printLinkedList(newHead)