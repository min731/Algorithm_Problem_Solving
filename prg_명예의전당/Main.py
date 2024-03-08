import heapq

def solution(k, score):
    answer = []
    res = []
    
    for s in score:
        heapq.heappush(res,s)
        tmp = heapq.nlargest(k,res)
        answer.append(tmp[::-1][0])

    return answer