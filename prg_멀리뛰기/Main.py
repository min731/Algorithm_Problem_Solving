def solution(n):

    dp = [0,1,2]

    for i in range(3,n+1):
        dp.append(dp[i-1]+dp[i-2])

    return dp[n]%1234567

# solution(1)
# solution(2)
# solution(3)
solution(4)
solution(5)
