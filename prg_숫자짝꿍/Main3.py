from collections import Counter

def solution(X, Y):
    answer = ''
    X = list(X)
    Y = list(Y)
    # print(X)
    # print(Y)
    countX = Counter(X)
    countY = Counter(Y)    
    com = []
    # print(countX)
    # print(countY)
    check = list(countX.keys() & countY.keys())
    # print(check)
    for k in check:
        valueX = countX[k]
        valueY = countY[k]
        
        for i in range(min(valueX,valueY)):
            com.append(k)
            
    # print(com)
    if not com:
        answer = "-1"
    else:
        tmp = sorted(com,reverse=True)
        
        if tmp[0]=="0":
            answer = "0"
        else:
            answer = "".join(tmp)
    
    return answer