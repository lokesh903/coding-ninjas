class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


def kReverse(head, k):
    cur = head 
    tempHead = None
    preEnd = None
    if cur is None or cur.next is None or k == 0:
        return head
    
    while cur:
        
        newHead,nextNode = reverseTillK(preEnd,cur,k)

        preEnd = cur
        cur = nextNode 
        if tempHead is None:
            tempHead = newHead
        
        
    return tempHead

def reverseTillK(preEnd,head,k):
    cur = head
    pre = None
    while cur and k:
        k-=1
        temp = cur.next 
        cur.next = pre
        pre = cur
        cur = temp
    if preEnd:
        preEnd.next = pre
    return pre,cur
        

def takeInput():
    inpList = list(map(int, input().split()))
    if not len(inpList) :
        return None
    
    cur = Node(inpList[0])
    head = cur
    for i in range(1, len(inpList)):
        cur.next = Node(inpList[i])
        cur = cur.next
    return head


def printll(head):
    cur = head
    while cur:
        print(cur.data, end=" ")
        cur = cur.next


head = takeInput()
k = int(input())
newHead = kReverse(head,k)
printll(newHead)
