def solution(cacheSize, cities):
    # Least recently used 캐시를 모방하는 자료구조를 구현한 뒤,
    # 시뮬레이션 하는 문제.
    # 자료구조에 대해서는
    # Cache hit, cache miss 두 가지 상황만 생각하면 된다.
    # cache hit이면, 해당 데이터가 최근에 hit 되었음을 업데이트 해주고,
    # cache miss이면, 가장 오래된 데이터를 제거 후 새로운 데이터를 캐시에 추가
    # 
    # 캐시 크기는 일정하므로, O(n) search를 허용해도 될 듯. 리스트로 쉽게 가자.
    # 
    cache, answer = [], 0
    for city in [c.lower() for c in cities]:
        # cache hit인 상황.
        if city in cache and cacheSize > 0: # cacheSize가 0일수도 있음에 주의!
            answer += 1
            # 비효율적이긴 한데, 이러면 쉽게 구현할 수 있다.
            cache.remove(city)
            cache.append(city)
        # 이하는 cache miss인 상황.
        elif len(cache) < cacheSize:
            answer += 5
            cache.append(city)
        else:
            answer += 5
            cache = cache[1:]
            cache.append(city)
            
    return answer
