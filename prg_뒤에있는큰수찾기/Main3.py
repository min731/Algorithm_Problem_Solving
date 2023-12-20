from collections import deque

def solution(numbers):
    answer = []
    
    # 4
    
    max_num = max(numbers)
    length = len(numbers)
    numbers = deque(numbers)
    
    while numbers:
        
        v = numbers.popleft()
        res = -1
        
        if v==max_num:
            answer.append(res) 
            continue
            
        for num in numbers:
            if v<num:
                res = num
                break
        answer.append(res)    
        
    return answer