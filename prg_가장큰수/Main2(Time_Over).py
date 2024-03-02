from itertools import permutations

def solution(numbers):
    answer = []

    for nums in permutations(numbers,len(numbers)):
        # print(list(nums))
        answer.append("".join([str(num) for num in nums]))

    print(answer)
    return  max(answer)

solution([9,997])