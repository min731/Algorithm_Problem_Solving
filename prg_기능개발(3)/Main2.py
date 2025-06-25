def solution(progresses, speeds):
    print(progresses)
    # print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer

if __name__ == "__main__":
    print(solution([93, 30, 55], [1, 30, 5]))
    print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
    # print(solution([100,100,100], [1, 1, 1]))
    # print(solution([85,100,90], [5, 1, 5]))
    # print(solution([80,95,90], [3, 1, 4]))
