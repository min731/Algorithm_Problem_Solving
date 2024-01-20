import sys
sys.setrecursionlimit(2000)

def dfs(k,nums,visitied,ans):
    if not visitied[k]:
        visitied[k]=True
        dfs(nums[k]-1,nums,visitied,ans)

    return 1


T = int(input())

for i in range(T):

    N = int(input())
    nums = list(map(int,input().split()))
    visitied = [False for j in range(N)]
    ans = 0
    
    for k in range(len(nums)):
        if not visitied[k]:
            ans += 1
        dfs(k,nums,visitied,ans)
    print(ans)