import copy

def solution(phone_book):
    
    # dic = {}
    # for num in phone_book:
    #     dic[num] = hash(num)
    # print(dic)
    
    for num in phone_book:
        # print("num : ",num)
        tmp = phone_book.copy()
        tmp.remove(num)
        
        dic = {}
        dic[num] = hash(num)
        
        for x in tmp:
            # print("x : ",x)
            if len(num)!=len(x):
                if hash(x[:len(num)]) in dic.values():
                    return False
            
        # for x in tmp:
        #     if num==x[:len(num)]:
        #         return False
            
    return True