from bisect import bisect

N = int(input())
array = list(map(int,input().split()))
array = sorted(array)
print(array)

max_idx = len(array)-1

M = int(input())
check = list(map(int,input().split()))

for x in check:
    print("x : ",x)
    print("value : ",bisect(array,x))
    v = bisect(array,x)

    if v-1 == 0 or v-1 == max_idx:
        if array[v-1] == x:
            print(1)
        else:
            print(0)
    else:
        print(1)