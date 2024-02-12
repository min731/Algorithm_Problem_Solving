def solution(n):
    
    if n==1:
        return 1
    elif n==2:
        return 2
    else:

        dp = [0]*(n+1)
        # print("dp :",dp)
        dp[1], dp[2] = 1, 2
        # print("dp :",dp)

        for i in range(3,n+1):
            dp[i] = (dp[i-2] + dp[i-1])%1000000007
        
        return dp[n]