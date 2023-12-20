def solution(numbers):
    answer = []
    
    # 4
    length = len(numbers)
    
    for i,num1 in enumerate(numbers[:length]):
        res = -1
        for j,num2 in enumerate(numbers[i+1:]):
            if num1<num2:
                res = num2
                break
        answer.append(res)
    
    # print("answer : ",answer)
    return answer