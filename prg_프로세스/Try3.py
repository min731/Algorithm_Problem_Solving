def solution(priorities, location):
    from collections import deque

    answer = 0
    queue = deque(priorities)

    while queue:

        print("----------------------")
        task = queue[location]
        max_n = max(list(queue))

        print("전 queue : ",queue)

        v = queue.popleft()

        if v == max_n:

            answer += 1

            if v == task:
                break

        else:
            queue.append(v)
        
        location -= 1

        print("location : " ,location)

        print("후 queue : ",queue)

        print("answer : ",answer)


    
    print("최종 answer : ",answer)

    return answer

# solution([2, 1, 3, 2],2)
solution([1, 1, 9, 1, 1, 1],0)