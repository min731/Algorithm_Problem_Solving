def binary_search(A,x):

    print("-----------------------")
    start = 0
    end = len(A)-1

    while start<=end:
        print("----------")
        mid = (start+end)//2
        print("start : ",start, "end : ",end, " mid : ",mid)

        if A[mid]==x:
            print(1)
            return
        elif A[mid]>x:
            end = mid-1
        else:
            start = mid+1
    print(0)

N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
A.sort()

for b in B:
    binary_search(A,b)