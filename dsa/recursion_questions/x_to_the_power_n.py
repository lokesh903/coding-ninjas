# Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to return the answer.

# Do this recursively.

#  TC = O(n)

# def power(x, n):
#     if n == 1:
#         return x
#     if n == 0:
#         return 1
#     return x*power(x,n-1)
    
def power(x, n):
    if n == 1:
        return x
    if n == 0:
        return 1
    if n % 2 == 0:
        small_power = power(x,n//2)
        big_power = small_power*small_power
        return big_power
    else:
        small_power = power(x,n//2)
        big_power = small_power*small_power*x
        return big_power


# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
x, n=list(int(i) for i in input().strip().split(' '))
print(power(x, n))
