def recursivePalindrome(s:str):
    
    s = s.replace(" ", "").lower()

    if len(s) < 1:
        return True
    elif s[0] == s[-1]:
        return recursivePalindrome(s[1:-1])
    else:
        return False
        
        

print(recursivePalindrome("I topi non avevano nipoti"))
