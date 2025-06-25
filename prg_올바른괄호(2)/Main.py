from collections import deque

def solution(s):
    
    answer = False
    s = deque(s)
    cnt = 0
    
    while s:
        
        x = s.popleft()
        
        if x == "(":
            cnt += 1
        else:
            cnt -= 1
        
        if cnt < 0:
            return False
    
    if cnt == 0:
        return True
    else:
        return False