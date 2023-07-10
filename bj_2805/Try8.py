def upper_bound(M,trees):

    start,end = 0, trees[-1]
    find = False
    cases = {}

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
            find = True
            cases[mid] = woods
            return cases,find,mid
        elif woods<M:
            end = mid
        else:
            cases[mid] = woods
            start = mid+1

    return cases,find,mid

N, M = map(int,input().split())

trees = list(map(int,input().split()))
trees = sorted(trees)
# print(trees)
# heights = [i for i in range(0,trees[-1]+1)]
# print(heights)
cases,find,mid= upper_bound(M,trees)
if find:
    print(mid)
else:
    min_k = trees[-1]
    for k,v in cases.items():
        if v >= M:
            if min_k>k:
                min_k  = k
    print(k)