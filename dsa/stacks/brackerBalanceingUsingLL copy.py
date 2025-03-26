# this is slow as this invlove creation of new nodes and push and pop operation on stack (LL)

from sys import stdin
class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class StackUsingLL():
    def __init__(self):
        self.head = None
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    def push(self,data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.size += 1
        
    def pop(self):
        if self.isEmpty():
            return -1
        else:
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return data
    
    def top(self):
        if self.isEmpty():
            return -1
        else:
            return self.head.data
    




def isBalanced(expression) :
	#Your code goes here
    stack = StackUsingLL()
    


    for char in expression:
        if char == "(":
            stack.push(char)
        if char == ")":
            if not stack.isEmpty() and stack.top() == "(":
                stack.pop()
            else:
                return False
    if stack.isEmpty():
        return True
    
    return False


           
            
        
        

#main
expression = stdin.readline().strip()

if isBalanced(expression) :
	print("true")

else :
	print("false")
