def solution(elements):
    from collections import deque

    elements = deque(elements)
    len_el = len(elements)
    answer = set()

    # 돌리기
    for i in range(1,len_el+1):
        tmp = elements.copy()

        for j in range(1,len_el+1):

            answer.add(sum(list(tmp)[:i]))

            tmp.rotate(1)
    answer.add(sum(list(tmp)))
    return len(answer)