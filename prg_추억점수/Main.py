def solution(name, yearning, photo):
    answer = []
    dic = {}
    
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    # print(dic)
    
    for p in photo:
        tmp = 0
        
        for x in p:
            try:
                tmp += dic[x]
            except:
                pass
        answer.append(tmp)
    
    return answer