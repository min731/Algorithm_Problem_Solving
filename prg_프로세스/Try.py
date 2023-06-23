def solution(priorities, location):
    from collections import deque

    answer = 0
    queue = deque(priorities)

    while True:
        
        print("----------------------------")
        print("전 queue : ",queue)

        max_n = max(queue)
        print("max_n : ",max_n)
        print("location : ",location)

        v = queue.popleft()

        if v == max_n:
            
            answer += 1

            if v == queue[location]:
                break
        else:
            queue.append(v)
        
        location -= 1

        print("후 queue : ",queue)
    
    print("answer : ",answer)
    return answer

solution([2, 1, 3, 2],2)