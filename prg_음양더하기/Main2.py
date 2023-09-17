def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)): 
        if signs[i]: #signs[i]인 경우 true
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer