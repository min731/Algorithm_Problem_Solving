def solution(n, times):
    answer = 0
    left = 1
    right = max(times)*n
    
    while left <= right:
        
        mid = (left+right)//2
        x = 0
        print(left,mid,right)
        
        for time in times:
            x += (mid//time)
            if n < x:
                right = mid-1
                break
                
        if n > x:
            left = mid+1
        else:
            answer = mid
            right = mid-1
            # print(answer)
        
    return answer

print(solution(6,[7,10]))
print(solution(3,[1, 2]))