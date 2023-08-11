def solution(n, lost, reserve):
    answer = 0

    # clothes = [1 for _ in range(n)]
    # print(clothes)

    clothes = []
    for i in range(n):
        # print("lost : ",lost)
        # print("clothes : ",clothes)
        if lost:
            if lost[0] == i+1:
                clothes.append(0)
                lost.pop(0)
                continue
        clothes.append(1)

    idx = 0
    while clothes:
        
        idx+=1
        v0 = clothes.pop(0)

        # if v0==1:
        #     continue
        # else:
        #     v1 = 


    # while clothes:

    
    return answer

solution(5,[2, 4],[1, 3, 5])