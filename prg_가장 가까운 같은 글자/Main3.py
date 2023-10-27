def solution(s):
    answer = []
    t = list(s)
    for i in range(len(t)):
        if t[i] in t[:i]:
            answer.append(i-t.index(t[i]))
            t[t.index(t[i])] = '0'
        else:
            answer.append(-1)
    return answer