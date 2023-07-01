def solution(scoville, K):
    answer = 0

    import heapq
    
    heapq.heapify(scoville)

    while True:

        print(scoville)

        min = heapq.heappop(scoville) 

        print(min)

        if min >= K:
            break
        
        if not scoville:
            answer = -1
            break

        min2 = heapq.heappop(scoville)

        new = min+min2*2

        heapq.heappush(scoville,new)
        answer += 1

    print("answer : ",answer)
    return answer

solution([1, 2, 3, 9, 10, 12],7)