def solution(x, y, n):
    answer = 0
    cnt = 0
    
    stack = [(x,cnt)]
    tmp = set()
    find = False
    
    while stack:
            
        now,cnt = stack.pop()
        
        # print("------------------")
        # print("now : ",now," cnt : ",cnt)
        
        if now==y:
            tmp.add(cnt)
            find = True

        if now+n<=y:
            stack.append((now+n,cnt+1))
        if now*2<=y:
            stack.append((now*2,cnt+1))
        if now*3<=y:
            stack.append((now*3,cnt+1))
    
    if find:
        return min(tmp)
    else:
        return -1