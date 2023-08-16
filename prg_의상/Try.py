def solution(clothes):
    import itertools
    print("-------------------------------------")
    answer = 0

    clothes_dict = {}

    for cloth in clothes:
        kind, name = cloth
        try:
            clothes_dict[name].append(kind)
        except:
            clothes_dict[name] = []
            clothes_dict[name].append(kind)

    print(clothes_dict)
    
    clothes_keys = clothes_dict.keys()
    n_keys = len(clothes_keys)

    for i in range(1,n_keys+1):
        for case in itertools.combinations(clothes_keys, i):
            print(list(case))

    print("-------------------------------------")
    return answer

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])