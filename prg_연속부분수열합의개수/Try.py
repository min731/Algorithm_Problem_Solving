def solution(elements):
    from collections import deque

    from itertools import combinations

    answer = set()

    for i in range(1,len(elements)+1):
        for case in combinations(elements,i):
            # print(case)

            answer.add(sum(case))

    print(answer)
    print(len(answer))

    return answer

solution([7,9,1,1,4])