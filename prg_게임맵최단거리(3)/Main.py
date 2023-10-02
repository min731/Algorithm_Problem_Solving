from collections import deque
def solution(maps):   

    n = len(maps)
    m = len(maps[0])

    # 동남서북
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    queue = deque([[0,0]])

    while queue:

        nowX, nowY = queue.popleft()

        if nowX==n-1 and nowY==m-1:
            return maps[n-1][m-1]
        
        for i in range(4):
            nextX = nowX+dx[i]
            nextY = nowY+dy[i]

            if nextX>=0 and nextX<n and nextY>=0 and nextY<m:
                if maps[nextX][nextY]==1:
                    maps[nextX][nextY] += maps[nowX][nowY]
                    queue.append([nextX,nextY])

    return -1


solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])