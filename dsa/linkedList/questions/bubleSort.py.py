
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def bubbleSort(head):
    
    
    pre = None
    cur = head
    counter = 0
    while cur:
        counter += 1 
        cur = cur.next
        
    for i in range(counter):
        cur = head
        pre = None
        while cur:
            if pre and pre.data > cur.data:
                cur.data, pre.data = pre.data,cur.data
            pre = cur
            cur = cur.next
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
newHead = bubbleSort(head)

printLinkedList(newHead)