def dfs(i,j,cnt):

    # stack으로 dfs 구현
    stack = [(i,j)]

    while stack:

        print("------------")
        for i in range(N):
            print(floor[i])
        print(stack)

        x,y = stack.pop()
        nowV = floor[x][y]

        if x+1<N and nowV == '|' and floor[x+1][y] == nowV:
            stack.append((x+1,y))
        elif y+1<M and nowV == '-' and floor[x][y+1] == nowV:
            stack.append((x,y+1))
        floor[x][y] = -1

    cnt += 1
    
    return cnt

N,M = map(int,input().split())

floor = []

for i in range(N):
    tmp = list(input())
    floor.append(tmp)

cnt = 0

# 전체 바닥 순회
for i in range(N):
    for j in range(M):
        # 순회한 곧은 -1로
        if floor[i][j] != -1:
            cnt = dfs(i,j,cnt)

print(cnt)