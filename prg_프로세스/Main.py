def solution(priorities, location):
    from collections import deque

    answer = 0
    queue = deque(priorities)
    idxes = deque([1 if i==location else 0 for i in range(len(queue))])

    print("idxes : ",idxes)

    while queue:


        print("----------------------")
        max_n = max(list(queue))

        print("전 queue : ",queue)

        v = queue.popleft()
        idx = idxes.popleft()

        if v == max_n:

            answer += 1

            if idx == 1:
                break

        else:
            queue.append(v)
            idxes.append(idx)

        print("location : " ,location)

        print("후 queue : ",queue)

        print("answer : ",answer)


    
    print("최종 answer : ",answer)

    return answer

solution([2, 1, 3, 2],2)
# solution([1, 1, 9, 1, 1, 1],0)