def solution(elements):
    from collections import deque

    elements = deque(elements)
    len_el = len(elements)
    answer = set()

    # 돌리기
    for i in range(1,len_el+1):
        # 더하기
        for j in range(len_el):
            print("elements : ",elements)
            # a = elements.popleft()
            # b = elements.popleft()
            answer.add(list(elements)[:])
            # elements.append(a)
            # elements.append(b)
            elements.rotate()

    print(answer)
    print(len(answer))

    return answer

solution([7,9,1,1,4])