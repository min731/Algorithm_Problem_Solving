def solution(numbers, target) : 
    
    answer = 0

    result = [0]

    while numbers:
        result2 = []
        num = numbers.pop()

        for res in result:
            result2.append(str(res)+ '+' + str(num))
            result2.append(str(res)+ '-' + str(num))

        print(result2)
        result = result2

    for res2 in result2:
        if res2 == target:
            answer += 1

    return answer

ans = solution([1, 1, 1, 1, 1],3)
# ans = solution([4, 1, 2, 1],4)
print(ans)