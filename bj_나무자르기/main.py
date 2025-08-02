N, M = map(int,input().split())
trees = list(map(int,input().split()))
# trees = sorted(trees)
ans = 0
# print(N,M)
# print(trees)

left = 0
right = max(trees)

while left <= right:
    mid = (left+right)//2

    # print(left,mid,right)
    amount = 0

    for tree in trees:
        diff = tree-mid
        if diff > 0:
            amount += diff
            if amount >= M:
                ans = mid
                left = mid+1 
                break 
    if amount < M:
        right = mid-1
    # print(amount)
print(ans)