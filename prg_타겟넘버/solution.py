# bfs
def solution(numbers, target) : 
    
    answer = 0
    
    from collections import deque
    
    # 값,인덱스
    queue = deque([[numbers[0],0],[numbers[0]*(-1),0]])
        
    while queue:
        
        v,n = queue.popleft()

        if n < len(numbers)-1:
            n += 1
            queue.append([v+numbers[n],n])
            queue.append([v-numbers[n],n])
        
        else:
            break
        
        print(queue)
        
    for x in queue:
        if x[0] == target:
            answer += 1
    
    return answer