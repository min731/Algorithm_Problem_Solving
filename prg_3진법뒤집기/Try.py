def solution(n):
    from collections import deque
    answer = 0
    tmp = deque([])
    while n!=1:
        if n%3==0:
            tmp.appendleft(n%3)
        else:
            tmp.appendleft(n%3)
        n = n//3
        # print(n)
    tmp.appendleft(1)
    print(tmp)
    quotient = 0
    for x in tmp:
        # print(x**quotient)
        answer += 3**quotient*x
        quotient += 1

    print(answer)
    return answer

solution(45)
solution(125)