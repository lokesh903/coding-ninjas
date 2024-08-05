n = int(input())
s = 0

def waysTo(n):
    if(n==0):
        return 1
    if(n==1 or n==2):
        return n
    return waysTo(n-1) + waysTo(n-2) + waysTo(n-3)

print(waysTo(n))