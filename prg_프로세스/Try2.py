def solution(priorities, location):
    from collections import deque

    answer = 0
    queue = deque(priorities)

    while True:

        task = queue[location]

        v = queue[0]

        if v >= task:

            if v == queue[location]:
                break
        else:
            queue.append(v)
        
        location -= 1

        if location < 0 :
            location = len(queue)-1

        print("후 queue : ",queue)
    
    print("answer : ",answer)
    return answer

solution([2, 1, 3, 2],2)