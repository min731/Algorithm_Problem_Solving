def solution(n, lost, reserve):

    print("---------------------------------")
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    print("new_lost : ",new_lost)
    print("new_reserve : ",new_reserve)

    for i in new_lost:
        print(new_reserve)
        if i - 1 in new_reserve:
            new_reserve.remove(i + 1)
        elif i + 1 in new_reserve:
            new_reserve.remove(i - 1)
        else:
            n-=1
        print("new_reserve : ",new_reserve)
        print("n : ",n)
        
    print("---------------------------------")
    return n

#            lost   reserve
# solution(5,[2, 4],[1, 3, 5])
# solution(5,[2, 4],[3])
# solution(3,[3],[1])
# solution(5,[2,4],[2,4])
solution(5,[1,2],[2,4])
# solution(5,[5],[2,4])