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

    new_clothes = []
    for idx,cloth in enumerate(clothes):

        res_can = False
        if reserve:
            if reserve[0] == idx:
                reserve.pop(0)
                res_can = True
        if cloth==0:
            if res_can:
                new_clothes.append(1)
            else:
                new_clothes.append(0)
            continue
        new_clothes.append(1)

    print(new_clothes)
    
    return answer

# solution(5,[2, 4],[1, 3, 5])
# solution(5,[2, 4],[3])
# solution(3,[3],[1])
solution(5,[2,4],[2,4])