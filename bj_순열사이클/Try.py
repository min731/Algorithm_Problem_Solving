T = int(input())

for i in range(T):
    print("-------------------------------------------------")
    N = int(input())
    nums = list(map(int,input().split()))
    print(nums)
    
    stack = [0]
    # check = [1]
    ans = 0

    while stack:

        print("--------")
        print("stack : ", stack)
        print("nums : ",nums)

        v = stack.pop()
        isCycle = False

        for num,idx in enumerate(nums):
            if num!=-1 and nums[v]==idx+1:
                print("nums[v] : ",nums[v], "idx+1", idx+1)
                stack.append(idx)
                nums[v] = -1
                isCycle = True
                break
        
        if not isCycle:
            ans += 1
            stack.a

    print("ans : ",ans)
