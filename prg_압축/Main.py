def solution(msg):
    answer = []
    
    numbers = { chr(i+64) : i for i in range(1,27)}
    print(numbers)
    
    now = 0
    w_c_cnt = 0
    for i,x in enumerate(msg):
        # print("---------------")
        # print(" i : ", i , " now : ",now)
        w = x
        
        if i==now:
            
            tmp = numbers[x]
            now_add = 0
            # print(" 찾음! : ",w)
            for j,y in enumerate(msg[i+1:]):

                # if i<j:
                w += y
                if w in numbers.keys():
                    tmp = numbers[w]
                    # print(" 찾음! : ",w)
                else:
                    w_c_cnt += 1
                    numbers[w] = 26+w_c_cnt
                    # print(" 추가! : ",w)
                    now += len(w)-1
                    break
            answer.append(tmp)

    # print(answer)
    return answer