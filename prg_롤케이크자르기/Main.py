def lower_bound(topping,start,end):
        
    while start<end:

        mid = (start+end)//2
        # print("--------------")
        # print("start :",start, "end : ",end,"mid : ",mid)

        old = len(set(topping[:mid]))
        young = len(set(topping[mid:]))

        if old>=young:
            end = mid
            
        elif old<young:
            start = mid+1
            
    return start

def upper_bound(topping,start,end):
    
    while start<end:

        mid = (start+end)//2
        # print("--------------")
        # print("start :",start, "end : ",end,"mid : ",mid)

        old = len(set(topping[:mid]))
        young = len(set(topping[mid:]))

        if old<=young:
            start = mid+1
            
        elif old>young:
            end = mid
            
    return end

def solution(topping):
    answer = 0
    
    start = 0
    end = len(topping)
    
    left = lower_bound(topping,start,end)
    right = upper_bound(topping,start,end)
    
    answer = right-left
    return answer