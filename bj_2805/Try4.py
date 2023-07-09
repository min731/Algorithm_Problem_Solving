def upper_bound(heights,M,trees):

    start,end = 0, len(heights)
    # all_woods = sum(trees)
    cases = {}

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
            # return heights[mid],cases
            print(heights[mid])
            exit()
        elif woods<M:
            end = mid
        else:
            cases[heights[mid]] = woods
            start = mid+1

    # return heights[mid],cases
    return cases

N, M = map(int,input().split())

trees = list(map(int,input().split()))
trees = sorted(trees)
heights = [i for i in range(0,trees[-1]+1)]
print(heights)
cases = upper_bound(heights,M,trees)
print(min(cases.keys()))