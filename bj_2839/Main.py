N = int(input())

ans = [-1]
bag = [5, 3]

# 가방 최대 갯수
max = N // bag[-1]

if N % bag[-1] != 0:
    max += 1

# 가방 최소 갯수 찾기
for i in range(max + 1):
    for j in range(max + 1):
        if N - bag[0] * i - bag[1] * j == 0:
            ans.append(i + j)
            # print(i, j, "체크")
            # print(bag[0] * i, bag[1] * j)
            del ans[0]

print(min(ans))
