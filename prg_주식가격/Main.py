from collections import deque
import copy

def solution(prices):
    answer = []
    
    prices = deque(prices)
    
    while prices:
        
        # print("----------------")
        price = prices.popleft()
        # print(price)
        
        tmp_prices = prices.copy()
        cnt = 0
        for tmp_price in tmp_prices:
            cnt += 1 
            if price>tmp_price:
                break
        answer.append(cnt)
        # print(answer)
    
    return answer