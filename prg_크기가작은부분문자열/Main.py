def solution(t, p):
    answer = 0 
    len_t = len(t)
    len_p = len(p)

    for i in range(len_t-len_p+1):
        # print(t[i:i+len_p])
        if t[i:i+len_p] <= p:
            answer += 1 

    print(answer)
    return answer

solution("3141592","271")
solution("500220839878","7")
solution("10203","15")
