def solution(cacheSize, cities):
    from collections import deque

    answer = 0
    
    cache = deque([])

    if cacheSize==0:
        answer = len(cities)*5
        print(answer)
        return answer

    for city in cities:
        city = city.upper()
        if not city in cache:
            if len(cache)<cacheSize:
                cache.appendleft(city)
            else:
                cache.pop()
                cache.appendleft(city)
            answer += 5
        else:
            cache.pop()
            cache.appendleft(city)
            answer += 1

    print(answer)   
    return answer   

# solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) #50
# solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]) #21
# solution(2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]) #60
# solution(5,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]) #52
# solution(2,["Jeju", "Pangyo", "NewYork", "newyork"]) #16
# solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) #25
solution(0,["LA","LA","LA"]) #15
solution(1,["LA","LA","LA"]) #7

