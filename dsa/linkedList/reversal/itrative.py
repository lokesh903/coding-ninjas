class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self,arr) -> None:
        cur = Node(arr[0])
        head = cur
        for i in range(1,len(arr)):
            newNode = Node(arr[i])
            cur.next = newNode
            cur = cur.next
        self.head = head
    def printLinkList(self):
        cur = self.head
        while cur:
            print(cur.data,end=' ')
            cur = cur.next

l = list(map(int,input().split()))

list1 = LinkedList(l)

# list1.printLinkList()

def revrseLinkedList(head):
    
    if not head:
        return head
        
    pre,cur = None,head
    
    while cur:
        nex = cur.next
        cur.next = pre
        pre = cur
        cur = nex
    
    head = pre
    return head

list1.head = revrseLinkedList(list1.head)
list1.printLinkList()
            
        
            
           
