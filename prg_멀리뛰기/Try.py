def solution(n):
    from collections import deque

    answer = 0
    # values = [i for i in range(n)]
    queue = deque([0])

    print(type(queue))
    while queue:

        print("queue : ",queue )
        v = queue.popleft()

        if v > n:
            continue
        elif v<n:
            queue.append(v+1)
            queue.append(v+2)
        else:
            answer += 1

    print(answer)
    return answer

# solution(10)
# solution(4)
# solution(3)
solution(1)