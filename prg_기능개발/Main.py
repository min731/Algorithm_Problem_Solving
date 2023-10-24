def solution(progresses, speeds):
    from collections import deque
    # progresses = deque(progresses)
    answer = []

    while progresses:
        print("-------------------")
        
        cnt = 0
        over_100 = True

        for idx,speed in enumerate(speeds):
            print("idx : ",idx)
            progresses[idx] += speed

            if over_100:
                if progresses[idx] >= 100:
                    cnt +=1 
                else:
                    over_100 = False

        print("progresses : ",progresses)

        progresses = progresses[cnt:]
        speeds = speeds[cnt:]

        # for _ in range(cnt):
        #     progresses.popleft()
        #     speeds.popleft()

        if cnt:
            answer.append(cnt)
    print(answer)
    return answer

solution([93, 30, 55],[1, 30, 5])
solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])