def solution(s):
    
    answer = False
    s = list(s)
    
    while s:
        
        last = s[0]
        s = s[1:]
        
        if s and last == "(":
            for idx, x in enumerate(s):
                if x == ")":
                    s.remove(")")
                    break
        else:
            return False

    return True