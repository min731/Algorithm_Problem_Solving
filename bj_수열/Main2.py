N, K = map(int,input().split())
# print(N,K)
nums = list(map(int,input().split()))
# print(nums)
length = len(nums) #10
end = K #2
start = end-K
max_hap = sum(nums[start:end])
stack = [(nums[0],max_hap)]

while end<length:
    
    print("stack : ",stack)
    front ,before_hap = stack.pop()
    now_hap = before_hap-front+nums[end]

    print("start : ",start, "end : ",end, " now_hap : ",now_hap)

    if now_hap>=max_hap:
        max_hap = now_hap
    start += 1
    stack.append((nums[start],now_hap))    
    end += 1
    # start += 1
    # stack.append((nums[start],now_hap))

print(max_hap)