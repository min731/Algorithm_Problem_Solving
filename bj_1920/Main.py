from bisect import bisect

N = int(input())
array = list(map(int,input().split()))
array = sorted(array)

max_idx = len(array)-1

M = int(input())
check = list(map(int,input().split()))

for x in check:
    v = bisect(array,x)

    if array[v-1] == x:
        print(1)
    else:
        print(0)