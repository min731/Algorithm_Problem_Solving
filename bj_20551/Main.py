import sys
input = sys.stdin.readline

def lower_bound(array,target):

    left , right = 0, len(array)
    
    while left<right:

        mid = (left+right)//2

        if array[mid] >= target:
            right = mid
        else:
            left = mid+1
        
        print("left : ",left,"right : ",right)

    if left > len(array)-1:
        return -1
    if array[left] ==target:
        return left
    else:
        return -1

        
N, M = map(int,input().split())

array = []

for _ in range(N):
    array.append(int(input()))
array = sorted(array)

query = []
for _ in range(M):
    query.append(int(input()))

for i in range(M):
    print(array)
    ans = lower_bound(array,query[i])
    print("ans : ",ans)

