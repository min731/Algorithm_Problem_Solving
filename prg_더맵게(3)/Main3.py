import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    size, cnt = len(scoville) - 1, 0
    f = heapq.heappop(scoville)
    while size > 0:
        s = heapq.heappop(scoville)
        f = heapq.heappushpop(scoville, f + s + s)
        if f >= K:
            return cnt + 1
        cnt += 1
        size -= 1
    return -1