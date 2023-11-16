
def solution(n, m, section):
    answer = 0
    
    end = section[0]+m-1
    answer += 1
    section = section[1:]
    
    # s = [1]
    # s = s[1:]
    # print(s)
    
    # print("section[1:] : ",section[1:])
    for sec in section:
        # print("-------------")
        # print("sec : ",sec)
        # print("end : ",end)
        
        if sec>end:
            answer += 1
            end = sec+m-1
        
    return answer