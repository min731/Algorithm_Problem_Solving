def solution(files):
    
    # HEAD : 문자
    # NUNMBER : 숫자, 0000, 0101
    # TAIL : 숫자 or 문자
    
    # 1) HEAD 사전순, 대소 구분X
    # 2) NUMBER : 숫자순, 앞 0 무시
    # 3) 같으면 원래 입력 순서 유지
    
    dic = {}
    idx = 0
    
    HEADs = set()
    
    for idx,file in enumerate(files):
        dic[file] = ('',0,idx) # HEAD 문자열, NUMBER 수, .소숫점
        
        endHEAD = [False,0]
        endNUMBER = [False,0]
        HEAD = ''
        NUMBER = 0
        
        for i,x in enumerate(file):
            
            if not endHEAD[0]:
                if x.isdigit():
                    endHEAD = [True,i]
                    HEAD = file[:i].upper() 
                    HEADs.add(HEAD)
            else:
                if not x.isdigit():
                    endNUMBER = [True,i]
                    NUMBER = int(file[endHEAD[1]:i])
                    break
        dic[file] = (HEAD,NUMBER,idx)
        print("-------------")
        print("file : ",file)
        print("endHEAD : ",endHEAD)
        print("endNUMBER : ",endNUMBER)
    
    print(dic)
    HEADs = sorted(list(HEADs))
    HEADs2 = dict()
    for i,HEAD in enumerate(HEADs):
        HEADs2[HEAD] = i+1
    print(HEADs)
    
    tmp = {}
    for k,v in dic.items():
        HEAD, NUMBER, idx = v
        tmp[k] = HEADs2[HEAD]*1000+NUMBER+ idx/1000
        
    print(sorted(tmp.items(), key = lambda x:x[1]))
    # print(sorted(tmp.items(), key = lambda x:x[1]))
    tmp = sorted(tmp.items(), key = lambda x:x[1])
    answer = []
    
    for x in tmp:
        answer.append(x[0])
    
    print(answer)
#     print(files)
#     files.sort()
#     print(files)
    
    return answer