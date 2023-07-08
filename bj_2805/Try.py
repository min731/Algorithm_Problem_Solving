def upper_bound1(heights,M):

    print("heights : ",heights)

    start = 0
    end = len(heights)-1

    while start<end:
        
        mid = (start+end)//2

        woods = sum(heights[mid:]) - heights[mid]*len(heights[mid:])

        print("start : ", start, ", end :",end, ", mid : ",mid)
        print("woods : ",woods)

        if woods==M :
            print(heights[mid])
            exit()
        elif woods<M :
            end = mid
        else :
            start = mid+1

    return mid

def upper_bound2(scope,heights,M):

    print("scope : ", scope)

    start = 0
    end = len(scope)-1
    trees = len(heights)
    max_woods = sum(heights)

    while start<end:
        
        mid = (start+end)//2

        woods = max_woods - scope[mid]*trees

        print("start : ", start, ", end :",end, ", mid : ",mid)
        print("woods : ",woods)

        if woods==M :
            print(scope[mid])
            exit()
        elif woods<M :
            end = mid
        else :
            start = mid+1

    return mid

N, M = map(int,input().split())
heights = list(map(int,input().split()))
heights = sorted(heights)

mid = upper_bound1(heights,M)
scope = [i for i in range(heights[mid]+1,heights[mid+1])]
heights = heights[mid+1:]
mid = upper_bound2(scope,heights,M)


print(scope[mid])