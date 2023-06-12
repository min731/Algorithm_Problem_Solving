def solution(maps):
    
    from collections import deque

    # answer = 0

    # x,y,이동
    queue = deque([[0,0,1]])

    # n X m 크기

    n = len(maps)
    m = len(maps[0])

    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True

    # 상우하좌
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    answer_list = []

    while queue:

        x,y,answer = queue.popleft()

        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]

            if newX >=0 and newX < n and newY >= 0 and newY < m:
                if maps[newX][newY] == 1:
                    if not visited[newX][newY]:
                        queue.append([newX,newY,answer+1])
                        visited[newX][newY] = True

        if x == n-1 and y == m-1:
            answer_list.append(answer)

    if len(answer_list) == 0:
        return -1

    return answer

# solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])
solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])