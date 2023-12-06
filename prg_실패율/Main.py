from collections import deque

def solution(N, stages):
    answer = {}
    res = []
    
    now = deque([i for i in range(1,N+1)])
    stages = sorted(stages)
    idx = 0

    while now:
        
        v = now.popleft()
        reaches = len(stages[idx:])
        
        if reaches==0:
            answer[v] = 0
            continue
        clears = 0
        
        for stage in stages[idx:]:
            if v==stage:
                clears += 1
                idx += 1
            else:
                break
        answer[v] = clears/reaches
        
    for ans in sorted(answer.items(), key = lambda x : x[1],reverse=True):
        res.append(ans[0])
    
    return res