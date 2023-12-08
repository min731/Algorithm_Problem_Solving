def solution(msg):
    answer = []
    
    numbers = { chr(i+64) : i for i in range(1,27)}
    print(numbers)
    
    now = 0
    w_c_cnt = 1
    for i,x in enumerate(msg):
        print("--------------")
        # print(" i : ",i, " now : ",now)
        
        if i==now:
            list(msg).pop()
            w = x
            tmp = []
            tmp.append(numbers[w])
            if msg[i:]:
                for y in msg[i:]:

                    if w in numbers.keys():
                        tmp.append(numbers[w])
                        print(" 찾음! : ",w)
                    else:
                        numbers[w] = 26+w_c_cnt
                        w_c_cnt += 1
                        print(" 추가! : ",w)
                        break
                    w += y

                answer.append(tmp[-1])
                now += len(w)-1 
            
    print(answer)
    
    return answer