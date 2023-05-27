def solution(brown, yellow):
    import math
    
    answer = [-1,-1]
    divisors = []
    
    for i in range(1,yellow+1):
        if yellow % i == 0 :
            divisors.append(i)
        
    len_div = len(divisors)
        
    for i in range(0,math.ceil(len_div/2)):
        
        if (divisors[i]+2) * (divisors[len_div-1-i]+2)-yellow == brown:
            answer[0] = divisors[len_div-1-i]+2
            answer[1] = divisors[i]+2
    
    return answer