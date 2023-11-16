
def solution(n, m, section):
    answer = 0
    
    end = section[0]+m-1
    answer += 1
    section = section[1:]
    
    for sec in section:

        if sec>end:
            answer += 1
            end = sec+m-1
        
    return answer