def solution(X, Y):
    answer = ''
    X = list(X)
    Y = list(Y)
    # print(X)
    # print(Y)
    com = []
    for i in range(10):
        # print(i,)
        countX = X.count(str(i))
        countY = Y.count(str(i))
        # print(i,countX,countY)
        
        for j in range(min(countX,countY)):
            com.append(str(i))
            
    # print(com)
    if not com:
        answer = "-1"
    else:
        answer = str(int("".join(sorted(com,reverse=True))))
    
    return answer