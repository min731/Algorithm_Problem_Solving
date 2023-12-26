from itertools import combinations,product

def solution(clothes):
    
    answer = 0
    sets = {}
    
    for cloth,kind in clothes:

        try:
            sets[kind].append(cloth)
        except:
            sets[kind] = []
            sets[kind].append(cloth)
    
    kinds = sets.keys()
    
    for i in range(len(sets.keys())):
        for cases in combinations(kinds,i+1):
            
            tmp = []
            for case in cases:
                tmp.append(sets[case])
                
            answer += len(list(product(*tmp)))
    
    return answer
