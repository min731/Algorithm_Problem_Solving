from collections import Counter
from itertools import cycle

def solution(answers):
    
    answer = []
    len_answers = len(answers)
    res = {str(i):0 for i in range(1,4)}
    
    ans_1 = [1,2,3,4,5] # (5개)
    ans_2 = [2,1,2,3,2,4,2,5] # (7개)
    ans_3 = [3,3,1,1,2,2,4,4,5,5] # (10개)
    
    cnt = 0
    for ans1,ans2,ans3 in zip(cycle(ans_1),cycle(ans_2),cycle(ans_3)):
        
        if cnt==len_answers:
            break
        
        if answers[cnt%len_answers]==ans1:
            res['1'] += 1
        if answers[cnt%len_answers]==ans2:
            res['2'] += 1
        if answers[cnt%len_answers]==ans3:
            res['3'] += 1
        cnt += 1
    
    most_v = Counter(res).most_common()[0][1]
    for k,v in Counter(res).most_common():
        
        if v==most_v:
            answer.append(int(k))
    
    answer.sort()

    return answer