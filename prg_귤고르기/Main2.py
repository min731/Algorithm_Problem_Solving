from collections import Counter
def solution(k, tangerine):
    answer = 0
    counter=Counter(tangerine)
    # {3: 2, 2: 2, 5: 2, 1: 1, 4: 1}
    sort_=sorted(counter.items(),key=lambda x:x[1],reverse=True)
    
    #정렬된 딕셔너리로 귤 개수 맞추기
    cnt=0
    for i in sort_:
        k-=i[1]
        answer+=1
        
        if k<=0:
            break
            
    return answer