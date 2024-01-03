from collections import deque

def solution(numbers, target) : 
    
    answer = 0
    length = len(numbers)
    queue = deque([(1,numbers[0]),(1,numbers[0]*(-1))])
    
    while queue:
        
        v = queue.popleft()
        cnt, value = v
        
        if cnt!=length:
            
            queue.append((cnt+1,value+numbers[cnt]))
            queue.append((cnt+1,value+numbers[cnt]*(-1)))
    
        else:
            if value==target:
                answer += 1

    return answer