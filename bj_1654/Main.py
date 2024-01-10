K,N = map(int,input().split())
ans = 0
lines = []

for _ in range(K):
    lines.append(int(input()))

# print(K,N)
# print(lines)

lines.sort()
# print(lines)

start, end = 1, lines[-1]

while start<=end:

    mid = (start+end)//2
    tmp = 0

    for line in lines:
        tmp += line//mid
    #print("tmp : ", tmp)

    if tmp>=N:
        start = mid+1
        ans = mid
    else:
        end = mid-1

    #print("start : ",start, "mid : ",mid," end : ",end)

print(ans)