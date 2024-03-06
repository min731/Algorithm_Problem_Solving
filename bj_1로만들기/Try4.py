from collections import deque

N = int(input())
mem = [0 for _ in range(N+1)]
print("mem : ",mem)

def get_cnt(x):

    if x==1:
        return 0
    elif x==2:
        return 1
    elif x==3:
        return 1

    queue = deque([[x,0]])
    print("-----------------------------------")
    print("x : ",x)

    while queue:
        print("-----------------")
        v, cnt = queue.popleft()
        print("v : ",v," cnt : ",cnt)

        if v==1: 
            return cnt
        
        if v%3==0:
            if mem[v//3]!=0:
                return mem[v//3]+cnt+1    
            queue.append([v//3,cnt+1])
        elif v%2==0:
            if mem[v//2]!=0:
                return mem[v//2]+cnt+1
            queue.append([v//2,cnt+1])
        elif mem[v-1]!=0:
            return mem[v-1]+cnt+1
        queue.append([v-1,cnt+1])

for i in range(1,N+1): 
    mem[i] = get_cnt(i)
print(mem)