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

    dp[n] = dp[n-2] + dp[n-1]

    return dp


def solution(n):
    answer = 0
    dp = [0 for _ in range(n+1)]

    dp = fibo(n,dp)

    print(dp)
    print(dp[n])

    answer = dp[n]%1234567

    return answer

solution(0)
solution(1)
solution(3)
solution(4)
solution(5)
solution(6)
