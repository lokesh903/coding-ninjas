class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def skipMdeleteN(head, M, N) :

    if head is None or M == 0:
        return None  # Return None if the list is empty or M is 0
    
    current = head
    prev = None
    
    while current:
        # Retain M nodes
        for _ in range(M):
            if current is None:
                return head  # If we run out of nodes, return the modified list
            prev = current
            current = current.next
            
        # Delete N nodes
        for _ in range(N):
            if current is None:
                break  # If there are no more nodes to delete
            current = current.next
            
        # Connect the retained part to the next segment
        prev.next = current  # Link the last retained node to the next retained node
    
    return head  # Return the new head of the modified list
        
        
            
            
        
   
        
    
    
    
    
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

M,N = list(map(int,input().split()))
head = takeinput()
newHead = skipMdeleteN(head, M, N)

printLinkedList(newHead)