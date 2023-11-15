from collections import Counter,deque
import copy

def solution(numbers):
    
    answer = set()
    numbers_copy = numbers.copy()
    numbers_copy = deque(numbers_copy)
    # numbers_copy.popleft()
    
    for number in numbers:
        print("----------------------------")
        numbers_copy.popleft()
        for number_copy in numbers_copy:
            # answer.append(number+number_copy)
            # print(number)
            print(number)
            print(number_copy)
            answer.add(number+number_copy)
        # numbers_copy.popleft()
    
    # answer = []
    # print(Counter(numbers))
    answer = sorted(list(answer))
    print(answer)
    return answer