import heapq
def solution(scoville, K):
    
    answer = 0
    heapq.heapify(scoville)
    keep = True
    
    while keep:
        
        keep = False
        x = heapq.heappop(scoville)
        # print("heappop: ",x)
        if not scoville and x < K:
            return -1
        if scoville and x < K:    
            keep = True
            y = heapq.heappop(scoville)
            heapq.heappush(scoville,x+y*2)
            answer += 1
    
    return answer