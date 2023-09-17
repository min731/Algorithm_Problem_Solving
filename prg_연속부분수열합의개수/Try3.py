def solution(elements):
    from collections import deque

    elements = deque(elements)
    len_el = len(elements)
    answer = set()

    # 돌리기
    for i in range(1,len_el+1):
        print("---------")
        # 더하기
        for j in range(1,len_el+1):
            print("elements : ",elements)
            answer.add(sum(list(elements)[:i]))
            print(answer)

            elements.rotate(i)


    print(answer)
    print(len(answer))

    return answer

solution([7,9,1,1,4])