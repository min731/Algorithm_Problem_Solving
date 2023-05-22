def solution(s):
    
    pl_sum = 0
    answer = True
    
    for pl in s:
        if pl=="(" :
            pl_sum+=1
        else:
            pl_sum+=-1
        if pl_sum<0 :
            answer = False
            break
    if pl_sum != 0 :
        answer = False
    
    return answer