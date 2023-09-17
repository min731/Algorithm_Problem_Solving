def solution(absolutes, signs):
    answer = 0

    for absolute, sign in zip(absolutes,signs):
        if sign==1:
            answer += absolute
        else:
            answer -= absolute

    return answer

solution([4,7,12],['true','false','true'])
solution([1,2,3],['false','false','true'])