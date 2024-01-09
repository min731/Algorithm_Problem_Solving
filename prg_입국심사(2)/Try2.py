def solution(n, times):
    answer = 0    
    start, end = 1, max(times)*n
    
    while start<=end:
        
        # print("---------------")
        mid = (start+end)//2
        tmp = 0
        
        print("start : ",start, "mid : ",mid,"end : ",end)

        for time in times:
            tmp += (mid//time)
        
        print("tmp : ",tmp)
        
        if n<=tmp:
            end=mid-1
            answer = mid
        else:
            start=mid+1
    
    print("answer : ",answer)
    return answer

# solution(6,[7, 10])
solution(3,[1,2])