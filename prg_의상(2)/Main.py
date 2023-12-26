from itertools import combinations,product

def solution(clothes):
    
    answer = set()
    sets = {}
    
    for cloth,kind in clothes:

        try:
            sets[kind].append(hash(cloth))
        except:
            sets[kind] = []
            sets[kind].append(hash(cloth))
    
    # print(sets)
    kinds = list(sets.keys())
    
    for i in range(len(sets.keys())):
        for cases in combinations(kinds,i+1):
            # print(list(cases))
            tmp = []
            for case in cases:
                tmp.append(sets[case])
            # print(tmp)
            # print(list(product(*tmp)))
                for v in list(product(*tmp)):
                    answer.add(sum(v))
    
    return len(answer)