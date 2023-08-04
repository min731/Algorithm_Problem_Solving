def solution(dartResult):
    answer = [0]
    from collections import deque

    dartResult = deque(list(dartResult))

    parser = {'S':1,'D':2,'T':3,'*':2,'#':-1}

    score = ''
    while dartResult:

        v = dartResult.popleft()

        score += v

        if v in ['S','D','T']:
            answer.append(int(score[:-1])**parser[v])

            if dartResult:

                v2 = dartResult.popleft()
                if v2 == '*':
                    answer[len(answer)-1] *= 2
                    answer[len(answer)-2] *= 2
                elif v2 == '#':
                    answer[-1] *= -1

                else: 
                    dartResult.appendleft(v2)

                score = ''

    return sum(answer)