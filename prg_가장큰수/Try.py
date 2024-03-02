def solution(numbers):
    answer = ''
    dic = {}
    
    for num in numbers:
        x = str(num)
        if len(x)!=3:
            dic[x] = [x+(3-len(x))*'99',(4-len(x))]  
        else:
            dic[x] = [x,0]
            
    print(dic)
#     numbers.sort(reverse=True)
    tmp = sorted(dic, key=lambda x:dic[x][0],reverse=True)
    print(tmp)
    
    for el in tmp:
        answer += str(el)
    
    print(answer)
    return  answer