def upper_bound(heights,M,trees):

    start,end = 0, len(heights)
    lack = trees[-1]
    over = 0

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
            if lack > heights[mid]:
                lack = heights[mid]
            end = mid
        else:
            if over < heights[mid]:
                over = heights[mid]
            start = mid+1

    return heights[mid],lack,over

N, M = map(int,input().split())

trees = list(map(int,input().split()))
trees = sorted(trees)
heights = [i for i in range(0,trees[-1]+1)]
print(heights)
heights, lack,over = upper_bound(heights,M,trees)

if over:
    print("get over")
    print(over)
else:
    print(lack)

# for k,y in ov.items():
#     if 
#     print(min(cases.keys()))