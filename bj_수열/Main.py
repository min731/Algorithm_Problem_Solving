N, K = map(int,input().split())
# print(N,K)
nums = list(map(int,input().split()))
# print(nums)
length = len(nums) #10
end = K #2
max_hap = 0

while end<=length:
    
    start = end-K

    # print("start : ",start, "end : ",end)
    now_hap = sum(nums[start:end])

    print("start : ",start, "end : ",end, " now_hap : ",now_hap)

    if now_hap>max_hap:
        max_hap = now_hap
    end += 1

print(max_hap)
