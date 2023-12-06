from collections import deque

def solution(N, stages):
    answer = {}
    res = []
    
    now = deque([i for i in range(1,N+1)])
    stages = sorted(stages)
    idx = 0
    # stages = deque(stages)
    
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
        # answer.append(clears/reaches)
        answer[v] = clears/reaches
    
    # print(answer)
    # print(answer.index(0)+1)
    # print(sorted(answer,key = lambda x : answer.index(x)+1))
    
    # for i, ans in enumerate(answer):
    # print(list(sorted(answer.items(), key = lambda x : x[1],reverse=True),key = lambda x : x[0]))
        
    for ans in sorted(answer.items(), key = lambda x : x[1],reverse=True):
        res.append(ans[0])
    
    return res