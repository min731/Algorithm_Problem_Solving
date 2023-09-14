def solution(n):
    from collections import deque

    answer = 0
    # values = [i for i in range(n)]
    queue = deque([n])

    while queue:

        print(queue)
        v = queue.popleft()

        if v>n:
            continue
        elif v<n:
            queue.append(v+1)
            queue.append(v+2)
        else:
            answer += 1

    print(answer)
    return answer%1234567

solution(2000)