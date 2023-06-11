# dfs

def solution(numbers, target) : 
    
    answer = 0
    
    # 값,인덱스
    stack = list([[numbers[0],0],[numbers[0]*(-1),0]])
        
    while stack:
        
        v,n = stack.pop()

        if n < len(numbers)-1:
            n += 1
            stack.append([v+numbers[n],n])
            stack.append([v-numbers[n],n])
        
        else:
            if v == target:
                answer += 1
    
    return answer