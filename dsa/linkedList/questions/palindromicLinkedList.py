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

# 1. find the mid
# 2. reverse after mid
# 3. check equivalace of elements

def getMid(head):
    
    slow, fast = head, head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

def reverseLinkedList(head):
    
    pre, cur = None, head
    
    while cur:
        nex = cur.next
        cur.next = pre
        pre = cur
        cur = nex
    
    return pre

def isPalindrome(head):
    
    if head is None or head.next is None:
        return True
    mid = getMid(head)
    reversedHead = reverseLinkedList(mid)
    frontHead = head
    while reversedHead and frontHead:
        if reversedHead.data != frontHead.data:
            return False
        reversedHead = reversedHead.next
        frontHead = frontHead.next
    return True
    
print(isPalindrome(list1.head))
            
        
         
         

           
