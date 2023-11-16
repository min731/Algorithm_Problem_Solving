from collections import deque

def solution(n, m, section):
    answer = 0
    
    # area = deque([i for i in range(1,n+1)])
    section = deque(section)
    
    while section:
        
        print("------------------")
        print("section : ",section)
        v = section.popleft()
        
        end = v+m-1
        for sec in section:
            if sec>end:
                answer +=1 
                break
            # section.popleft()

        print("answer : ",answer)
        print("section : ",section)
    
    return answer