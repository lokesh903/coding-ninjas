def isPalindrome(string: str) -> bool:
    if len(string) == 1 or len(string) == 0 :
        return True
    return string[0] == string[-1]  and  isPalindrome(string[1:-1])

st=input()
print(isPalindrome(st))

# print(st[1:-1])
# sucuhhucus