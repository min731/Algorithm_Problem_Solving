def solution(n):
    from collections import deque
    answer = 0
    tmp = deque([])
    quotient = 0
    while n!=1:
        remainder = n%3
        if remainder==0:
            tmp.appendleft(remainder)
        else:
            tmp.appendleft(remainder)
        n = n//3
        print("tmp : ",tmp)
        add_qu = 3**quotient
        print("add_qu : ", add_qu)
        add = add_qu*remainder
        print("add : ",add)
        answer += add
        quotient += 1
    print(tmp)
    # answer += 3**quotient*n
    print(answer)
    return answer

solution(45)
# solution(125)