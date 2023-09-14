def solution(n):
    answer = 0
    tmp = []
    while n!=1: 
        tmp.append(n%3)
        n = n//3
        print(n)
    tmp.append(1)
    print(tmp)
    quotient = 0

    for x in tmp[::-1]:
        answer += 3**quotient*x
        quotient += 1

    print(answer)
    return answer

solution(45)
solution(125)