from sys import stdin

def arrayEquilibriumIndex(arr, n) :
    #Your code goes here
    if len(arr) == 0:
        return -1
        
    ls = arr[0]
    rs = 0
    for i in range(1,n):
        rs += arr[i]
     
    if rs == ls:
            return 0
    for i in range(1,n):
        
        rs -= arr[i]
        if rs == ls:
            return i
        ls += arr[i]

    return -1


    




























#Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    print(arrayEquilibriumIndex(arr, n))

    t-= 1