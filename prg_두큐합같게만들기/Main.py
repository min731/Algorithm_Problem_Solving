from collections import deque

def solution(queue1, queue2):
    answer = -2
    # half = len(queue1)
    # max_chance = len(queue1)*2-1
    # chance = 0
    # target = sum(queue1+queue2)/2

    queue1 = deque(queue1)
    queue2 = deque(queue2)
    hap1 = sum(queue1)
    hap2 = sum(queue2)
    chance = 0
    max_chance = len(queue1)*3
    isFind = False

    while chance<max_chance:
        
        if hap1>hap2:
            v1 = queue1.popleft()
            queue2.append(v1)
            hap1 -= v1
            hap2 += v1
        elif hap1<hap2:
            v2 = queue2.popleft()
            queue1.append(v2)
            hap2 -= v2
            hap1 += v2
        else:
            isFind = True
            break
        chance += 1
    if isFind:
        return chance
    else:
        return -1
solution([3, 2, 7, 2],[4, 6, 5, 1])
# solution([1, 2, 1, 2],[1, 10, 1, 2])
# solution([1, 1],[1, 5])

