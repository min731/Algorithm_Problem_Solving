def solution(clothes):
    import itertools
    from functools import reduce
    
    answer = 0

    clothes_dict = {}

    for cloth in clothes:
        name,kind = cloth
        try:
            clothes_dict[kind].append(name)
        except:
            clothes_dict[kind] = []
            clothes_dict[kind].append(name)

    clothes_keys = clothes_dict.keys()
    n_keys = len(clothes_keys)

    for i in range(1,n_keys+1):
        for case in itertools.combinations(clothes_keys, i):
            n_case = len(case)
            multiple_list = [len(clothes_dict[case[j]])for j in range(n_case)]
            answer += reduce(lambda x, y: x * y, multiple_list)

    return answer

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])