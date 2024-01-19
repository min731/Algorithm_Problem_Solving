T = int(input())

for i in range(T):
    print("-------------------------------------------------")
    N = int(input())
    nums = list(map(int,input().split()))
    # print(dic)
    dic = {}
    for idx,num in enumerate(nums):
        dic[idx] = num

    stack = [0] # 인덱스 삽입
    # check = [1]
    ans = 0

    while stack:

        print("--------")
        print("stack : ", stack)
        print("nums : ",dic)

        v = stack.pop()
        isCycle = False
        
        if dic[v] != -1:
            stack.append(dic[v]-1)
            dic[v] = -1
            isCycle = True

        if not isCycle:
            ans += 1
            for k,v in dic.items():
                if v!=-1:
                    stack.append(k)
                    break

    print("ans : ",ans)
