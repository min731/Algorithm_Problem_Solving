def binary_search(array,target):

    start , end = 0, len(array)-1

    while start<=end:

        mid = (start+end)//2

        if array[mid] == target:
            return mid
        if array[mid] < target:
            start = mid+1
        else:
            end = mid-1

    return -1

        
N, M = map(int,input().split())

array = []

for _ in range(N):
    array.append(int(input()))
array = sorted(array)

query = []
for _ in range(M):
    query.append(int(input()))

print("---------")
for i in range(M):
    ans = binary_search(array,query[i])
    print(ans)