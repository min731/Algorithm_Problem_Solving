def solution(price, money, count):
    return max(0, price * sum(range(1,count+1))-money)