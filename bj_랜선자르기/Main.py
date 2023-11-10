def binary_search(lines,N):
    start = 1
    end = lines[0]
    ans_list = []

    if N <= sum([line//end for line in lines]):
        # return end 
        print(end)
        return

    # cnt = 0
    while start<=end:
        
        cnt = 0

        # cnt += 1
        # if cnt==10:
        #     return 0
        mid = (start+end)//2

        for line in lines:
            cnt += line//mid

        if cnt >= N:
            start = mid+1
            ans_list.append(mid)
        
        # if cnt > N:
        #     start = mid+1
        if cnt < N:
            end = mid-1

    return print(max(ans_list))

K,N = map(int,input().split())

ans = -1

lines = []
for _ in range(K):
    lines.append(int(input()))
# print(lines)
lines.sort(reverse=True)

binary_search(lines,N)