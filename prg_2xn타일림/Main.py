from collections import deque

def solution(n):
    answer = 0
    queue = deque([n])
    
    while queue:
        
        v = queue.popleft()
        
        if v==0:
            answer += 1
            
        if v-2>=0:
            queue.append(v-2)
        if v-1>=0:
            queue.append(v-1)
        
    return answer%1000000007