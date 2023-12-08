def solution(msg):
    answer = []
    
    numbers = { chr(i+64) : i for i in range(1,27)}
    print(numbers)
    
    w_c_cnt = 0
    for idx,x in enumerate(msg):
        print("--------------------")
        
        w = ''
        tmp = []
        for y in msg[idx:]:
            
            w += y
            if w in numbers.keys(): 
                tmp.append(numbers[w])
                print(w)
            else:
                
                print("추가! : ",w)
                w_c_cnt += 1
                numbers[w] = 26+w_c_cnt
                break
        
        # print(tmp[-1])
        
        answer.append(tmp[-1])
        
    print(answer)
    
    return answer