from collections import deque

def solution(begin, target, words):
    
    answer = 0
    queue = deque([[0,begin]])
    
    while queue:
        
        cnt, now = queue.popleft()
        
        if now == target:
            answer = cnt
            break
            
        for word in words:
            diff = 0
            for w1,w2 in zip(now,word):
                if w1!=w2:
                    diff += 1
            if diff == 1:
                words.remove(word)
                queue.append([cnt+1,word])
            
    return answer