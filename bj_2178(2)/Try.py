N, M = map(int,input().split())
# print(N,M)

maps = []
for i in range(N):
    data = list(map(int,list(input())))
    maps.append(data)

for i in range(N):
    print(maps[i])

#우하좌상
dx = [0,1,0,-1]
dy = [1,0,-1,0]

from collections import deque

queue = deque([[0,0]])

cnt = 1

while queue:

    x,y = queue.pop()

    for i in range(4):
        newX = x+dx[i]
        newY = y+dy[i]

        if newX>=0 and newX<N and newY>=0 and newY<M:
            if maps[newX][newY]==1:
                queue.appendleft([newX,newY])
                maps[newX][newY] = maps[x][y]+1

print("-----------------------")
for i in range(N):
    print(maps[i])
print("-----------------------")
print(maps[N-1][M-1])
