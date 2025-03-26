
from sys import stdin

#Following is the structure of the node class for a Singly Linked List
class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None


class Stack :

    #Define data members and __init__()
    
    def __init__(self):
        self.head = None
        self.size = 0



    '''----------------- Public Functions of Stack -----------------'''


    def getSize(self) :
        #Implement the getSize() function
        return self.size



    def isEmpty(self) :
        #Implement the isEmpty() function
        return self.size == 0



    def push(self, data) :
        #Implement the push(element) function
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        
    def pop(self) :
        #Implement the pop() function
        if self.isEmpty():
            return -1
        else:
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return data



    def top(self) :
        #Implement the top() function
        if self.isEmpty():
            return -1
        else:
            return self.head.data
        




#main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0 :

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1 :
        data = int(inputs[1])
        stack.push(data)

    elif choice == 2 :
        print(stack.pop())

    elif choice == 3 :
        print(stack.top())

    elif choice == 4 : 
        print(stack.getSize())

    else :
        if stack.isEmpty() :
            print("true")
        else :
            print("false")

    q -= 1