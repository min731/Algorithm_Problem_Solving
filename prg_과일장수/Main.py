def solution(k, m, score):
    answer = 0
    
    score = sorted(score, reverse=True)
    
    for i in range(0,len(score),m):

        if len(score[i:i+m])==m:
            answer += score[i:i+m][-1]*m
    return answer