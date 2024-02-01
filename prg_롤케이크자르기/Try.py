def solution(topping):
    answer = set()
    
    start = 0 # 0부터
    end = len(topping) # 8까지
    
    cnt = 0
    while start<end:
        cnt +=1
        
        if cnt==10:
            break
            
        mid = (start+end)//2
        print("--------------")
        print("start :",start, "end : ",end,"mid : ",mid)
        # 0 8 4
        
        old = len(set(topping[:mid]))
        young = len(set(topping[mid:]))
        
        if old==young:
            print("같음!")
            # if mid not in answer:
            answer.add(mid)
            start += 1
        elif old<young:
            end = mid+1
        else:
            start = mid+1
                  
    answer = len(answer)
    return answer