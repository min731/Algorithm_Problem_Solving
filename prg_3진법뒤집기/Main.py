def solution(n):
    
    answer = ''
    
    while n>0:
        n,re = divmod(n,3)
        answer += str(re)
    print(answer)
    print(int(answer,3))
    return int(answer,3)

solution(45)
solution(125)