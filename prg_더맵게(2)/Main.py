import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville:
        
        # print("------------")
        # print(scoville)
        v1 = heapq.heappop(scoville)
        
        if v1<K:
            if len(scoville)==0:
                answer = -1
                break
            
            if scoville:
                v2 = heapq.heappop(scoville)
                heapq.heappush(scoville,v1+(v2)*2)
                answer += 1
        else:
            break
    
    # print(scoville)
    
    return answer