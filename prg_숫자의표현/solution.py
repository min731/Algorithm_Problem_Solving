def solution(n):
    answer = 0
    
    # i는 1~n 까지
    for i in range(1,n+1):
        sum = 0
        
        # j는 i~n까지
        for j in range(i,n+1):
            sum += j
            if sum == n :
                answer += 1
                break
            if sum > n :
                break
                
    return answer