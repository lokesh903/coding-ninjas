# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(string):
    # Please add your code here
    if string =='':
        return ""
    ch = string[0]
    if len(string) == 1:
        return ch
    i,j = 0,1
    skip = 1
    while ( j < len(string)) and (string[i] == string[j]):
        if len(string) == 2:
            return ch 
        skip+=1
        i+=1
        j+=1
    ans = ch + removeConsecutiveDuplicates(string[skip:])
    return ans

# Main
# string = input().strip()
print(removeConsecutiveDuplicates('xxxyyyzwwzzz'))
