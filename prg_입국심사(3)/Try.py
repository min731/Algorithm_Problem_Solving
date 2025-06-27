def solution(n, times):
    answer = 0    
    check = [i for i in range(1,times[-1]*n+1)]
    # print(check)
    times = sorted(times)
    
    left = 0
    right = check[-1]
    
    while left < right:
        
        mid = (left+right)//2
        x = 0
        print(left,mid,right)
        
        for time in times:
            x += (check[mid]//time)
            if n < x:
                right = mid-1
                break
                
        if n > x:
            left = mid+1
        else:
            answer = check[mid]
            right = mid-1
            print(answer)
        
    return answer

# print(solution(6,[7,10]))
print(solution(3,[1, 2]))