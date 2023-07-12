def solution(number, k):
    answer = [] # Stack
    
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        print(answer)
        answer.append(num)
    print(answer)
        
    
    print(''.join(answer[:len(answer) - k]))
    return ''.join(answer[:len(answer) - k])

solution(['4123'],2)