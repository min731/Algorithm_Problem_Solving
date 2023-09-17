def solution(elements):
    from collections import deque

    elements = deque(elements)
    len_el = len(elements)
    answer = set()

    # 돌리기
    for i in range(1,len_el+1):
        tmp = elements.copy()
        print("---------")
        # 더하기
        for j in range(1,len_el+1):
            print("elements : ",tmp)
            answer.add(sum(list(tmp)[:i]))
            print(answer)

            tmp.rotate(1)

    answer.add(sum(list(tmp)))
    print(answer)
    print(len(answer))

    return answer

solution([7,9,1,1,4])
# solution([2,1,4])