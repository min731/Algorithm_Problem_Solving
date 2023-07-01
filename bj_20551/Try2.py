def lower_bound(array,target):

    left , right = 0, len(array)
    print(array)
    while left<right:

        mid = (left+right)//2

        print("start : ",left, "end : ",right, "mid : ",mid)
        print("array[mid] : ",array[mid],"target : ",target)

        if array[mid] < target:
            left = mid+1
        else:
            right = mid

    print("left : ",left,"right : ",right)

    if left == len(array):
        return -1

    if array[left] == target:
        return left

        
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
    ans = lower_bound(array,query[i])
    print(ans)