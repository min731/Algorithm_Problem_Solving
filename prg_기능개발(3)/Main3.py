import math

def solution(progresses, speeds):
    answer = []
    rest = []
    temp = []

    size = len(progresses)

    for i in progresses:
        rest.append(100 - i)

    for i in range(size):
        temp.append(math.ceil(rest[i] / speeds[i]))

    cnt = 0
    p = temp[0]
    for i in range(len(temp)):
        if p < temp[i]:
            answer.append(cnt)
            p = temp[i]
            cnt = 0
        cnt += 1
    answer.append(cnt)


    return answer

if __name__ == "__main__":
    # print(solution([93, 30, 55], [1, 30, 5]))
    # print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
    print(solution([100,99,97], [1, 1, 1]))
    print(solution([100,100,100], [1, 1, 1]))
    print(solution([85,100,90], [5, 1, 5]))
    print(solution([80,95,90], [3, 1, 4]))
