T = int(input())

for i in range(T):
    print("-------------------------------------------------")
    N = int(input())
    nums = list(map(int,input().split()))
    print(nums)
    
    stack = [0] # 인덱스 삽입
    # check = [1]
    ans = 0

    while stack:

        print("--------")
        print("stack : ", stack)
        print("nums : ",nums)

        v = stack.pop()
        isCycle = False
        
        if nums[v] != -1:
            stack.append(nums[v]-1)
            nums[v] = -1
            isCycle = True

        if not isCycle:
            ans += 1
            for idx,num in enumerate(nums):
                if num!=-1:
                    stack.append(idx)
                    break


    print("ans : ",ans)
