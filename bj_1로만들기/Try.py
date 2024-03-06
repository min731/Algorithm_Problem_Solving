from collections import deque

# N = int(input())
# mem = [0 for _ in range(1000001)]

def make_one(x):
    
    queue = deque([[x,0]])

    while queue:

        print("------------")
        v, cnt = queue.popleft()
        print("v : ",v , "cnt : ",cnt)

        if v==1:
            return v,cnt
        
        if v%3==0:
            queue.append([int(v/3),cnt+1])
        if v%2==0:
            queue.append([int(v/2),cnt+1])
        queue.append([v-1,cnt+1])


v,cnt = make_one(10)
print(v)
print(cnt)