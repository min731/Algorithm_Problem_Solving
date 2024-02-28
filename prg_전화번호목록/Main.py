def solution(phone_book):
    
    
    dic = {}
    for num in phone_book:
        dic[num] = 1
    # print(dic)
    
    for num in phone_book:
        tmp = ""
        for x in num:
            tmp += x
            if tmp in dic and tmp !=num:
                return False
            
    return True