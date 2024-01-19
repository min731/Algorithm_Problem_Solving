def fibo(n,dp):

    if n == 0:
        dp[0] = 0
        return dp
    
    elif n == 1:
        dp[1] = 1
        return dp
    
    if dp[n-2] == 0:
        dp = fibo(n-2,dp)
    if dp[n-1] == 0:
        dp = fibo(n-1,dp)

    dp[n] = (dp[n-2] + dp[n-1]) %1234567

    return dp


def solution(n):
    answer = 0
    dp = [0 for _ in range(n+1)]

    dp = fibo(n,dp)


    answer = dp[n]

    return answer