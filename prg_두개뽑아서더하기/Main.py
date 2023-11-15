from collections import Counter,deque
import copy

def solution(numbers):
    
    answer = set()
    numbers_copy = numbers.copy()
    numbers_copy = deque(numbers_copy)
    
    for number in numbers:
        numbers_copy.popleft()
        for number_copy in numbers_copy:
            answer.add(number+number_copy)
    answer = sorted(list(answer))

    return answer