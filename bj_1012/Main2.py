T = int(input())

def bfs(farm,x,y):

    from collections import deque

    queue = deque([[x,y]])
    visited[x][y] = True
    
    while queue:

        v = queue.popleft()
        
        x = v[0]
        y = v[1]

        farm[x][y] = 0
            
        for k in range(4):
            Newx = x + dx[k]
            Newy = y + dy[k]

            if Newx >=0 and Newx < M and Newy >= 0 and Newy < N:
                if not visited[Newx][Newy]:
                    if farm[Newx][Newy] == 1:
                        queue.append([Newx,Newy])
                        visited[Newx][Newy] = True

        # print(queue)

# 상우하좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]      

for _ in range(T):
    M, N, K = map(int,input().split())

    farm = [[0]*N for m in range(M)]
    visited = [[False]*N for m in range(M)]

    for k in range(K):

        i,j = map(int,input().split())
        farm[i][j] = 1

    ans = 0
    for x in range(M):
        for y in range(N):

            if farm[x][y] == 1:
                ans += 1
                bfs(farm,x,y)
    
    print(ans)