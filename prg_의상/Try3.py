def solution(clothes):
    import itertools
    from functools import reduce
    print("-------------------------------------")
    answer = 0

    clothes_dict = {}
    clothes_cnt = 0

    for cloth in clothes:
        kind, name = cloth
        clothes_cnt += 1
        try:
            clothes_dict[name].append(clothes_cnt)
        except:
            clothes_dict[name] = []
            clothes_dict[name].append(clothes_cnt)

    print(clothes_dict)
    
    clothes_keys = clothes_dict.keys()
    n_keys = len(clothes_keys)

    for i in range(1,n_keys+1):
        for case in itertools.combinations(clothes_keys, i):
            print(list(case))
            n_case = len(case)
            multiple_list = [len(clothes_dict[case[j]])for j in range(n_case)]
            answer += reduce(lambda x, y: x * y, multiple_list)

    print("-------------------------------------")
    print(answer)
    return answer

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])