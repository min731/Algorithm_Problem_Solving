from collections import Counter
from functools import reduce

def solution(clothes):
    # 1. 의상 종류별 Counter를 만든다.
    counter = Counter([type for clothe, type in clothes])

    print(counter)
    print(counter.values())
    # 2. 모든 종류의 count + 1을 누적하여 곱해준다
    answer = reduce(lambda acc, cur: acc*(cur+1), counter.values(),1) - 1
    print(answer)
    return answer

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
# print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))

# 출처: https://coding-grandpa.tistory.com/88 [개발자로 취직하기:티스토리]