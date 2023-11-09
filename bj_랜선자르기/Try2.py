def binary_search(lines,N):
    start = 0
    end = lines[0]

    # cnt = 0
    while start<=end:
        
        cnt = 0

        # cnt += 1
        # if cnt==10:
        #     return 0
        mid = (start+end)//2

        print("------------------")
        print("start : ",start)
        print("mid : ",mid)
        print("end : ",end)

        for line in lines:
            cnt += line//mid
            print("line//lengths[mid] : ",line//mid)
        print("cnt : ",cnt)

        if cnt >= N:
            print("cnt : ",cnt)
            print(" K : ",N)
            return mid
        
        # if cnt > N:
        #     start = mid+1
        if cnt < N:
            end = mid-1

K,N = map(int,input().split())

ans = -1

lines = []
for _ in range(K):
    lines.append(int(input()))
# print(lines)
lines.sort(reverse=True)
print(lines)

ans = binary_search(lines,N)
print(ans)