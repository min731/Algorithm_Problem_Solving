def solution(name, yearning, photo):
    answer = []
    dic = {}
    
    for k,v in zip(name,yearning):
        dic[k] = v
    
    for p in photo:
        tmp = 0
        
        for x in p:
            try:
                tmp += dic[x]
            except:
                pass
        answer.append(tmp)
    
    return answer