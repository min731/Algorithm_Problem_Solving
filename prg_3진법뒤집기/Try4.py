def solution(n):
    from collections import deque
    answer = 0
    tmp = deque([])
    while n!=1: 
        tmp.appendleft(n%3)
        n = n//3
        print(n)
    tmp.appendleft(1)
    print(tmp)
    quotient = 0

    while tmp:
        v = tmp.popleft()
        if v!=0:
            answer += 3**quotient*v
        quotient += 1

    print(answer)
    return answer

solution(45)
solution(125)