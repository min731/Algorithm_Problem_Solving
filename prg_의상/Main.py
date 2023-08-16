def solution(clothes):
    # 1. 옷을 종류별로 구분하기
    hash_map = {}

        # 옷    # 종류
    for clothe, type in clothes:
        hash_map[type] = hash_map.get(type, 0) + 1
    
    print(hash_map)

    # 2. 입지 않는 경우를 추가하여 모든 조합 계산하기
    answer = 1
    for type in hash_map:
        print("type : ",type)   
        answer *= (hash_map[type] + 1)
    
    # 3. 아무종류의 옷도 입지 않는 경우 제외하기
    return answer - 1

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])