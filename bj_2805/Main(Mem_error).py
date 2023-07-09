def upper_bound(heights,M,trees):

    start,end = 0, len(heights)
    lack = {}
    over = {}

    while start<end:

        mid = (start+end)//2
        woods = 0

        for tree in trees:
            wood = tree - heights[mid]
            if wood > 0:
                woods += wood

        if woods==M:
            print(heights[mid])
            exit()
        elif woods<M:
            lack[heights[mid]] = woods
            end = mid
        else:
            over[heights[mid]] = woods
            start = mid+1

    return heights[mid],lack,over

N, M = map(int,input().split())

trees = list(map(int,input().split()))
trees = sorted(trees)
heights = [i for i in range(0,trees[-1]+1)]

heights, lack,over = upper_bound(heights,M,trees)

if over:
    print("get over")
    print(max(over.keys()))
else:
    print(min(lack.keys()))

# for k,y in ov.items():
#     if 
#     print(min(cases.keys()))