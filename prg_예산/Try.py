def solution(d, budget):
    answer = 0
    
    d.sort()
    print(d)
    for el in d:
        budget-=el
        if budget<0:
            break
        answer += 1

    print(answer)
    return answer

solution([1,3,2,5,4],9)
solution([2,2,3,3],10)