from collections import deque

def solution(order):
    answer = 0
    length =len(order)
    order = deque(order)
    con1 = deque([i for i in range(1,length+1)]) # queue
    con2 = [] # stack
    
    while order:
        
#         print("------------------")
#         print("order : ",order)
        
        find  = False
        x = order.popleft()
        
        if con2 and con2[-1]==x:
            con2.pop()
            answer += 1
            find = True
            # print("con1 : ",con1)
            # print("con2 : ",con2)
            # print(x," 찾음!")
            continue
        
        while con1:
            b1 = con1.popleft() 
            if b1==x:
                answer+=1
                find = True
                # print("con1 : ",con1)
                # print("con2 : ",con2)
                # print(x," 찾음!")
                break
            else:
                con2.append(b1)
        
        if not find:
            break
        
    return answer