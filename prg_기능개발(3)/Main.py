from collections import deque

def solution(progresses, speeds):
    
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)

    while progresses:
        
        # print(progresses)
        success = 0
        
        if progresses[0] >= 100:
            while progresses:
                now_pro = progresses.popleft()
                if now_pro >= 100:
                    success += 1
                    speeds.popleft()
                else:
                    progresses.appendleft(now_pro)
                    break

        for idx, (pro, spe) in enumerate(zip(progresses, speeds)):
            progresses[idx] += spe
        
        if success > 0:
            answer.append(success)
        
    return answer