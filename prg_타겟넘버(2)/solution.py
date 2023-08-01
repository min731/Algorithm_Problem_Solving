def solution(numbers, target) : 
    
    answer = 0

    result = [0,0]

    while numbers:
        result2 = []
        num = numbers.pop()

        for res in result:
            result2.append(res+num)
            result2.append(res-num)

        result = result2

    for res2 in result2:
        if res2 == target:
            answer += 1

    return answer/2