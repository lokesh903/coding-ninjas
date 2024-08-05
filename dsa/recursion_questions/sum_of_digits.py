

n = int(input())
sm = 0
def sod(sm,num):
    if(num <= 0):
        print(sm)
        return
    digit = num%10
    sm += digit
    sod(sm,num//10)
sod(sm,n)
    