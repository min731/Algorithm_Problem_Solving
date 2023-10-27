def solution(s):
    from collections import deque
    
    s = list(s)
    
    answer = []
    check = []
    s_copy = deque(s.copy())

    while s_copy:
        
        v = s_copy.popleft()

        if v not in check:
            answer.append(-1)
            check.append(v)
        else:
            reverse_check = check[::-1]
            answer.append(reverse_check.index(v)+1)
            check.append(v)
    
    return answer