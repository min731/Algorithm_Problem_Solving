N,M = map(int,input().split())

floor = []
visited = []

for i in range(N):
    tmp = list(input())
    floor.append(tmp)
    visited.append([False for _ in range(M)])

# print(floor)
# print(visited)

stack = [(0,0)]
# visited[0][0] = True

# 우하좌상
dx = [0,1,0,-1]
dy = [1,0,-1,0]

cnt = 0

while stack:

    print("------------")
    for i in range(N):
        print(floor[i])
    print(stack)

    x,y = stack.pop()
    
    v = floor[x][y]
    
    for i in range(4):

        newX = x+dx[i]
        newY = y+dy[i]

        if newX>=0 and newX<N and newY>=0 and newY<M:

            if floor[newX][newY] != -1:
                if abs(x-newX) == 1 and floor[x][y] == '|' and floor[newX][newY] == '|':
                    floor[x][y] = -1
                    floor[newX][newY] = -1
                    cnt += 1
                elif abs(x-newX) == 1 and floor[x][y] == '-' and floor[newX][newY] == '-':
                    floor[x][y] = -1
                    floor[newX][newY] = -1
                    cnt += 1
                stack.append((newX,newY)) 

print(cnt)