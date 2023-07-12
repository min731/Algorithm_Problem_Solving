def solution(number, k):
    from itertools import combinations
    
    number = list(number)
    indexes = [idx for idx in range(len(number))]
    value = 0

    for case in combinations(indexes,k):
        case = list(case)
        origin = list(number)
        cnt = 0
        for i in case:
            del origin[int(i-cnt)]
            cnt += 1
        now = int("".join(origin))
        if now > value:
            value = now
    print(value)
    return str(value)

solution("1924",2)
solution("1231234",3)
solution("4177252841",4)
