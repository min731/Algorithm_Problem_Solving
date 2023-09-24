def solution(number):
    answer = 0

    from itertools import combinations

    for case in combinations(number,3):

        if sum(case)==0:
            answer += 1
        print(case)

    print(answer)
    return answer

solution([-2, 3, 0, 2, -5])
solution([-3, -2, -1, 0, 1, 2, 3])
solution([-1, 1, -1, 1])