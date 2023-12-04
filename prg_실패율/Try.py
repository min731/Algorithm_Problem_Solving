from collections import Counter

def solution(N, stages):
    answer = []
    
    players = len(stages)
    
    stages = Counter(stages)
    print(stages)
    print(stages.most_common()) 
    
    res = {str(i+1):0 for i in range(N)}
    # res = Counter(res)

    for value,cnt in stages.most_common():
        res[str(value)] = (players-cnt)/cnt
        #answer.append(value/players)

    #answer.sort()
    #print(answer)
    
    res = Counter(res)
    print(res.most_common())
    
    return res 
