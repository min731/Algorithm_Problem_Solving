N = str(input())

ans = -1
nums = list(N)
nums = sorted(nums,reverse=True)


# 30의 배수
# 3의 배수 : 모든 수의 합이 3의 배수
# 10의 배수 : 끝자리가 0
if '0' not in nums:
    print(-1)
else:
    n_sum = 0 
    for i in range(len(nums)):
        n_sum += int(nums[i])

    if n_sum%3 == 0:
        print("".join(nums))
    else:
        print(-1)