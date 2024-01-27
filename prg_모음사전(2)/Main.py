from itertools import product

def solution(word):
    
    words = ['A', 'E', 'I', 'O', 'U']
    answer = 0
    tmp = []
    
    for i in range(1,6):
        for x in product(words,repeat=i):
            tmp.append("".join(x))
            
    tmp.sort()
    answer = tmp.index(word)+1

    return answer