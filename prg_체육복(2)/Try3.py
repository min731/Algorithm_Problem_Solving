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

    check_clothes = []

    print("---------------------------------------------------------------")
    for idx,cloth in enumerate(clothes):
        print("idx , cloth : ",idx,cloth)

        if cloth == 0:
            if reserve:
                if reserve[0] == idx+2 or reserve[0] == idx+1 or reserve[0] == idx:
                    check_clothes.append(1)
                    reserve.pop(0)
                else:
                    check_clothes.append(0)
                print("reserve : ",reserve)
                print("check_clothes : ",check_clothes)
                continue
        else:
            check_clothes.append(1)
        print("reserve : ",reserve)
        print("check_clothes : ",check_clothes)


    print("reserve : ",reserve)
    print("check_clothes : ",check_clothes)

    print("---------------------------------------------------------------")

    return answer

solution(5,[2, 4],[1, 3, 5])
# solution(5,[2, 4],[3])
# solution(3,[3],[1])
# solution(5,[2,4],[2,4])