def solution(number, k):
    from itertools import combinations
    
    answer = ''
    number = list(number)
    indexes = [idx for idx in range(len(number))]

    for case in combinations(indexes,k):
        # case = (m,n)
        case = list(case)
        # origin = "".join(number)
        origin = list(number)
        # case[0] += 1
        print(origin)
        print(case)
        cnt = 0
        for i in case:
            print(i-cnt)
            del origin[int(i-cnt)]
            cnt += 1
        print(origin)

    return answer


solution("1924",2)