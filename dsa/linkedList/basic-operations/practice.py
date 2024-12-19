class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert(self,data):
        if not self.head:
            self.head=Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
        return self.head

    def insertFromList(self,ls):
        lastNode = self.head
        
        if lastNode:
            while lastNode.next:
                lastNode = lastNode.next
                
            for i in ls:
                lastNode.next = Node(i)
                lastNode = lastNode.next
        else:
            self.head = Node(ls[0])
            lastNode  = self.head
            for i in range(1,len(ls)):
                lastNode.next = Node(ls[i])
                lastNode = lastNode.next
                
        return self.head

    def insertFromInput(self):
        ls = list(map(int, input().split()))
        self.insertFromList(ls)
        return self.head



    def display(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            current = self.head
            while current:
                print(current.data, end=" ")
                current = current.next
            print()
        return

temp = LinkedList()
temp.insert(1)
temp.insert(2)
temp.insert(3)
temp.insert(4)
temp.insert(5)
temp.display()

temp.insertFromList([6,7,8,9,10])
temp.display()

temp.insertFromInput()
temp.display()