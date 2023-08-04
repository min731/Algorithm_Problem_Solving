def solution(dartResult):
    res = []
    cnt = 0 #한판 점수
    dartResult=dartResult.replace("10", "t")
    
    for n in dartResult:
        if n.isnumeric():
            cnt += int(n)
            continue
        elif n == 't': #10점
            cnt += 10
            continue
        elif n == 'S':
            res.append(cnt)
        elif n == 'D':
            res.append(cnt ** 2)
        elif n == 'T':
            res.append(cnt ** 3)
        elif n == '*': #스타상이고 두 판 이상했을 때
            if len(res)>1:
                res[-1] *= 2  #해당점수 2배
                res[-2] *= 2  #바로 전 점수 2배
            else : # 한판만 했으면
                res[-1] *= 2
        elif n == '#': 
            res[-1] *= -1
        cnt=0 #한판점수 초기화
    return(sum(res))