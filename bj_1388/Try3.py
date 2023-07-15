def dfs(stack,floor,cnt):

    while stack:

        print("------------")
        for i in range(N):
            print(floor[i])
        print(stack)

        x,y = stack.pop()
        nowV = floor[x][y]
        
        if nowV != -1:
            floor[x][y] = -1

            for i in range(4):

                newX = x+dx[i]
                newY = y+dy[i]


                if newX>=0 and newX<N and newY>=0 and newY<M:

                    nextV = floor[newX][newY]

                    if abs(x-newX) == 1 and nowV == '|' and nextV == '|':
                        stack.append((newX,newY))
                        dfs(stack,floor,cnt)
                    if abs(y-newY) == 1 and nowV == '-' and nextV == '-':
                        stack.append((newX,newY))
                        dfs(stack,floor,cnt)
                    cnt += 1
                    # dfs(stack,floor,cnt)

N,M = map(int,input().split())

floor = []
visited = []

for i in range(N):
    tmp = list(input())
    floor.append(tmp)
    # visited.append([False for _ in range(M)])

# print(floor)
# print(visited)

stack = [(0,0)]
# visited[0][0] = True

# 우하좌상
dx = [0,1,0,-1]
dy = [1,0,-1,0]

cnt = 0

dfs(stack,floor,cnt)

print(cnt)