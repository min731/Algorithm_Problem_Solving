def solution(cacheSize, cities):
    from collections import deque

    answer = 0
    
    cache = deque([])

    if cacheSize==0:
        answer = len(cities)*5

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
            cache.remove(city)
            cache.appendleft(city)
            answer += 1

    return answer   