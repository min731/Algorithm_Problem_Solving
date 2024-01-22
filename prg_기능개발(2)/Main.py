from collections import deque

def solution(progresses, speeds):
    answer = []
    
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while progresses:
        
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        first_prg = progresses[0]
        deploy = 0        
        
        if first_prg>=100:
            for prg in progresses:
                if prg>=100:
                    deploy += 1
                else:
                    break
            answer.append(deploy)
            
            for i in range(deploy):
                progresses.popleft()
                speeds.popleft()
                
    return answer