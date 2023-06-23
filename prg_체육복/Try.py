def solution(n, lost, reserve):

    answer = 0

    items = [1 for i in range(n)]

    print(items)

    for i in lost:
        items[i-1] = 0
    
    print(items)

    for i in reserve:
        items[i-1] += 1
    print(items)

    for i in range(1,len(items)):
        if items[i] == 2:
            if items[i-1] == 0:
                items[i] = 1
                items[i-1] = 1
            elif items[i+1] == 0:
                items[i] = 1
                items[i+1] = 1


    print(items)

    for x in items:
        if x != 0:
            answer += 1

    print(answer)

    return answer

solution(5,[2, 4],[1, 3, 5])
solution(5,[2, 4],[3])
solution(3,[3],[1])

