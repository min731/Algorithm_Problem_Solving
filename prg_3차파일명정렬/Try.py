def solution(files):
    
    # HEAD : 문자
    # NUNMBER : 숫자, 0000, 0101
    # TAIL : 숫자 or 문자
    
    # 1) HEAD 사전순, 대소 구분X
    # 2) NUMBER : 숫자순, 앞 0 무시
    # 3) 같으면 원래 입력 순서 유지
    
    dic = {}
    idx = 0
    
    HEADs = []
    
    for idx,file in enumerate(files):
        dic[file] = idx
        # file = ''.join(filter(str.isalpha, file))
        
        endHEAD = (False,0)
        endNUMBER = (False,0)
        for i,x in enumerate(file):
            
            if not endHEAD[0]:
                if not x.isalpha():
                    endHEAD = (True,i)
                    HEADs.append(file[:i])
            else:
                if x.isalpha():
                    endNUMBER = (True,i)
                    break
        print("-------------")
        print("file : ",file)
        print("endHEAD : ",endHEAD)
        print("endNUMBER : ",endNUMBER)
            
        # print(file)
        
    
#     print(files)
#     files.sort()
#     print(files)
    
    
    
    
    answer = []
    return answer