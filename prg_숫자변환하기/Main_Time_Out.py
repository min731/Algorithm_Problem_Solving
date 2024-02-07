from collections import deque

def solution(x, y, n):
    answer = 0
    cnt = 0
    
    queue = deque([(x,cnt)])
    
    while queue:
            
        now,cnt = queue.popleft()
        
        # print("------------------")
        # print("now : ",now," cnt : ",cnt)
        
        if now==y:
            answer = cnt
            return answer

        if now+n<=y:
            queue.append((now+n,cnt+1))
        if now*2<=y:
            queue.append((now*2,cnt+1))
        if now*3<=y:
            queue.append((now*3,cnt+1))
    
    return -1