from collections import deque

def solution(land):
    answer = 0
    
    # 이전 인덱스, 현재 점수
    queue = deque([(0,0,1),(0,1,2),(0,2,3),(0,3,5)])
    length = len(land)

    while queue:
        
        # print("--------------")
        # print("queue : ",queue)
        x,y,score = queue.popleft()
        
        if length>x+1:
        
            for idx,value in enumerate(land[x+1]):

                if y!=idx:
                    new = score+value
                    queue.append((x+1,y,new))
                    if new > answer:
                        answer = new

    return answer