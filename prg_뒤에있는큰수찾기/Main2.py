from collections import deque

def solution(numbers):
    answer = []
    
    # 4
    length = len(numbers)
    numbers = deque(numbers)
    
    while numbers:
        
        v = numbers.popleft()
        res = -1
        
        for num in numbers:
            if v<num:
                res = num
                break
        answer.append(res)    
        
    return answer