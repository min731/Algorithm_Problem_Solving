from collections import deque

def solution(msg):
    answer = []
    
    numbers = { chr(i+64) : i for i in range(1,27)}
    # print(numbers)
    
    wc_cnt = 1
    for i in range(len(msg)-1):
        
        print("-------------------")
        w = msg[i]
        w_c = list(msg[i:])
        
        is_in = False
        while len(w_c)>1:
            
            print(w_c)
            if ",".join(w_c) in numbers.keys():
                print(",".join(w_c))
                answer.append(numbers[",".join(w_c)])
                is_in = True
                break
            else:
                w_c.pop()
        
        if not is_in:
            # w_c.pop()
            answer.append(numbers[",".join(w_c)])
            numbers[w+msg[i+1]] = 26+wc_cnt
            wc_cnt += 1
        print(answer)
        

    print(numbers)
    # for i in range(size):
        
    # print(answer)
    return answer

solution("KAKAO")