from collections import deque

N = int(input())
mem = [0 for _ in range(N+1)]

def make_one(x):
    queue = deque([[1,0]])

    while queue:
        v, cnt = queue.popleft()
        
        if v==x: 
            return cnt
        
        queue.append([v*3,cnt+1])
        queue.append([v*2,cnt+1])
        queue.append([v+1,cnt+1])

for i in range(1,N+1):
    mem[i] = make_one(i)
print(mem[N])
