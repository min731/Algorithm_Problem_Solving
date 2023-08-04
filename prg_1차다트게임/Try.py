def solution(dartResult):
    answer = [0]
    from collections import deque

    dartResult = deque(list(dartResult))
    print(dartResult)

    parser = {'S':1,'D':2,'T':3,'*':2,'#':-1}

    score = ''
    while dartResult:

        print("dartResult : ",dartResult)

        v = dartResult.popleft()

        # 1S
        # 2D
        score += v

        if v in ['S','D','T']:
            answer.append(int(score[:-1])**parser[v])

            if dartResult:

                print("옵션 전 : ", answer)
                v2 = dartResult.popleft()
                if v2 == '*':
                    answer[len(answer)-1] *= 2
                    answer[len(answer)-2] *= 2
                elif v2 == '#':
                    answer[-1] *= -1

                else: 
                    dartResult.appendleft(v2)
                
                print("옵션 후 : ", answer)

                score = ''

        

    return sum(answer)


ans = solution('1S2D*3T')
print("ans : ",ans)
print("----------------------------------------")
ans = solution('1D2S#10S')
print("ans : ",ans)

# a = [0,11]
# print(a[len(a)-2:len(a)])