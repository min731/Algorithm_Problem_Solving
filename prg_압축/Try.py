from collections import deque

def solution(msg):
    answer = []
    
    numbers = { chr(i+64) : i for i in range(1,27)}
    # print(numbers)
    
    size = len(msg)
    
    msg = deque(list(msg))
    # print(msg)
    w = ''
    wc_cnt = 1
    idx = 0
    
    while msg:
        
        v = msg.popleft()
        w += v
        
        # print(numbers.keys())
        
        for m in msg:
            if w in numbers.keys():
                answer.append(numbers[w])
                # numbers[w+msg[0]] = 26+wc_cnt
                numbers[w] = 26+wc_cnt
                wc_cnt += 1
                print(w)
                w = ''
                break
            else:
                w += m 
    
    # for i in range(size):
        
    print(answer)
    return answer