def solution(d, budget):
    answer = 0
    
    d.sort()

    for el in d:
        budget-=el
        if budget<0:
            break
        answer += 1

    return answer