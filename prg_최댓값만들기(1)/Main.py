def solution(numbers):
    answer = 0
    
    nums = sorted(numbers)
    
    answer = nums[-1]*nums[-2]
    print(answer)
    return answer


solution([0, 31, 24, 10, 1, 9])