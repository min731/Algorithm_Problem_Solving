def upper_bound1(heights,M):

    start = 0
    end = len(heights)-1

    while start<end:
        
        mid = (start+end)//2

        woods = sum(heights[mid:]) - heights[mid]*len(heights[mid:])

        if woods==M :
            print(heights[mid])
            exit()
        elif woods<M :
            end = mid
        else :
            start = mid+1

    return mid

def upper_bound2(scope1,heights,M):

    start = 0
    end = len(scope1)-1
    trees = len(heights)
    max_woods = sum(heights)

    while start<end:
        
        mid2 = (start+end)//2

        woods = max_woods - scope1[mid2]*trees

        if woods==M :
            print(scope1[mid2])
            exit()
        elif woods<M :
            end = mid2
        else :
            start = mid2+1

    return print(scope1[mid])

N, M = map(int,input().split())
heights = list(map(int,input().split()))
heights = sorted(heights)

mid = upper_bound1(heights,M)
scope1 = [i for i in range(heights[mid]+1,heights[mid+1])]
heights = heights[mid+1:]
upper_bound2(scope1,heights,M)