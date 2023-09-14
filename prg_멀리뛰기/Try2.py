def solution(n):
    from collections import deque

    answer = 0
    # values = [i for i in range(n)]
    queue = deque([[0]])

    while queue:

        print("queue : ",queue )
        v = queue.popleft()
        print("v : ",v)

        if sum(v) > n:
            continue
        elif sum(v) < n:
            addv1 = v.append(1)
            addv2 = v.append(2)

            queue.append(addv1)
            queue.append(addv2)
        else:
            answer += 1

    print("answer : ",answer)
    return answer

# solution(10)
# solution(4)
# solution(3)
solution(1)
solution(2)
solution(3)
solution(4)