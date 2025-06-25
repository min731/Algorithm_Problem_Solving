from collections import deque

def solution(s):
    
    answer = False
    
    while s:
        
        s = deque(s)
        last = s.popleft()
        
        if s and last == "(":
            for idx, x in enumerate(s):
                if x == ")":
                    s = list(s)
                    del s[idx]
                    break
        else:
            return False

    return True