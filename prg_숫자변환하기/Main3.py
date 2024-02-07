from collections import deque

def solution(x, y, n):
    answer = 0
    cnt = 0
    
    queue = deque([(y,cnt)])
    
    while queue:
            
        now,cnt = queue.popleft()
        
        # print("------------------")
        # print("now : ",now," cnt : ",cnt)
        
        if now==x:
            answer = cnt
            return answer

        if now-n>=x:
            queue.append((now-n,cnt+1))
        if now/2>=x and now%2==0 :
            queue.append((now/2,cnt+1))
        if now/3>=x and now%3==0 :
            queue.append((now/3,cnt+1))
    
    return -1