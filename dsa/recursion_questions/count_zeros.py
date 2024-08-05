n = int(input())
cnt = 0

def count_zero(cnt,n):
    if n == 1 or n == 0:
        print(cnt)
        return
    digit = n%10
    if digit == 0:
        cnt+=1
    count_zero(cnt,n//10)

if n==0 :
    print(1)
else:
    count_zero(cnt,n)