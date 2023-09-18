def solution(price, money, count):
    answer = -1

    answer = money-sum([i*price for i in range(1,count+1)])
    
    if answer>=0:
        return 0
    else:
        return abs(answer)

solution(3,20,4)