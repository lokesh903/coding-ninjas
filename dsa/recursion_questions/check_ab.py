def check_string(s):
    if not s:
        return True
    
    if s[0] != 'a':
        return False
    
    # If the string starts with 'a', handle the following possibilities:
    if len(s) == 1:
        return True  # The string is just "a", which is valid.
    
    if s[1] == 'a':
        # If after 'a' there's another 'a', continue checking the rest of the string.
        return check_string(s[1:])
    
    if s[1:3] == 'bb':
        # If after 'a' there's "bb", continue checking the rest of the string.
        if len(s) == 3:
            return True  # The string is just "bb", which is valid.
        elif s[3] == 'a':
            # If after "bb" there's an 'a', continue checking from that point.
            return check_string(s[3:])
        else:
            # If after "bb" there's anything else, it's invalid.
            return False
    
    # If none of the valid conditions are met, the string is invalid.
    return False




s = input()
print(check_string(s))
# if(check_string(s)):
#     print('true')
# else:
#     print('false')