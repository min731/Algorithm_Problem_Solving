def get_divisor(num,limit,power):
    
    divisors = 0
    
    for i in range(1,num+1):
        if num%i==0:
            divisors += 1
        if divisors > limit:
            divisors = power
            break
    
    return divisors

def solution(number, limit, power):
    
    answer = 0
    
    for i in range(1,number+1):
                    
        divisors = get_divisor(i,limit,power)
        
        answer += divisors
        # if divisors>limit:
        #     answer += power
        # else:
        #     answer += divisors
    
    return answer