def upper_bound(M,trees):

    start,end = 0, trees[-1]

    while start<end:

        mid = (start+end)//2
        woods = 0

        for tree in trees:
            wood = tree - mid
            if wood > 0:
                woods += wood

        print("start : ", start, ", end :",end, ", mid : ",mid)
        print("woods : ",woods)

        if woods==M:
            return mid
        elif woods<=M:
            end = mid
        else:
            start = mid+1

    return start-1

N, M = map(int,input().split())

trees = list(map(int,input().split()))
trees = sorted(trees)
# print(trees)
# heights = [i for i in range(0,trees[-1]+1)]
# print(heights)
height = upper_bound(M,trees)
print(height)
