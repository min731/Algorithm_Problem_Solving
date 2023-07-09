def upper_bound(heights,M,trees):

    start,end = 0, len(heights)
    # all_woods = sum(trees)
    lack = {}
    over = {}
    find = False

    while start<end:

        mid = (start+end)//2
        woods = 0

        for tree in trees:
            wood = tree - heights[mid]
            if wood > 0:
                woods += wood

        print("start : ", start, ", end :",end, ", mid : ",mid)
        print("woods : ",woods)


        if woods==M:
            find = True
            return heights[mid],cases,find
        elif woods<M:
            lack[heights[mid]] = woods
            end = mid
        else:
            over[heights[mid]] = woods
            start = mid+1

    return heights[mid],cases,find

N, M = map(int,input().split())

trees = list(map(int,input().split()))
trees = sorted(trees)
heights = [i for i in range(0,trees[-1]+1)]
print(heights)
height,cases,find = upper_bound(heights,M,trees)
print(cases)
if find:
    print("find!")
    print(height)
else:
    for k,y in cases.items():
        if 
    print(min(cases.keys()))