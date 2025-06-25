from collections import deque

def solution(progresses, speeds):
    
    answer = []
    progresses = deque(progresses)

    while progresses:
        
        print(progresses)
        success = 0
        
        if progresses[0] >= 100:
            while progresses:
                now = progresses.popleft()
                if now >= 100:
                    success += 1
                else:
                    progresses.appendleft(now)
                    break

        for idx, (pro, spe) in enumerate(zip(progresses, speeds)):
            progresses[idx] += spe
        
        if success > 0:
            answer.append(success)
        
    return answer

if __name__ == "__main__":
    # print(solution([93, 30, 55], [1, 30, 5]))
    # print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
    # print(solution([100,100,100], [1, 1, 1]))
    # print(solution([85,100,90], [5, 1, 5]))
    print(solution([80,95,90], [3, 1, 4]))
