def solution(numbers):

    check = [i for i in range(10)]

    for x in numbers:
        if x in check:
            check[x] = 0

    return sum(check)