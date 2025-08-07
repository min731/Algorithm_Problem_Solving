def solution(n, times):

    left, right = 0, max(times) * n
    
    while left <= right:
        mid = (left+right)//2
        cnt = 0
     	
        for time in times:
            cnt += mid//time
            
            # 더 많이 심사함
            if cnt >= n:
                break

        # 더 많이 심사함
        if cnt >= n:
            answer = mid
            right = mid -1
        
        # 적게 심사함
        else :
            left = mid + 1

    return answer