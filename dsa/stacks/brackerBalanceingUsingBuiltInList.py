import sys
from sys import stdin



def isBalanced(expression):
    stack = []

    for char in expression:
        if char == "(":
            stack.append(char)  # Push to stack
        elif char == ")":
            if not stack:  # No matching opening bracket
                return False
            stack.pop()  # Remove the matching opening bracket
    
    # If the stack is empty, all parentheses are matched
    return len(stack) == 0


           
            
        
        

#main
expression = sys.stdin.read().strip() 

if isBalanced(expression) :
	print("true")

else :
	print("false")
