def solution(maps):

    x_len = len(maps)
    y_len = len(maps[0])

    # 우하좌상
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    from collections import deque

    queue = deque([(0,0,1)])

    while queue:

        x,y,n = queue.pop()

        if x==x_len-1 and y==y_len-1:
            return n

        maps[x][y] = -1

        print("------------------------")
        print("x, y, n :",x,y,n)
        for map in maps:
            print(map)
        print("------------------------")

        for i in range(4):
            
            newX = x+dx[i]
            newY = y+dy[i]

            if newX>=0 and newX<x_len and newY>=0 and newY<y_len:
            
                if maps[newX][newY] == 1:
                    queue.appendleft((newX,newY,n+1))

    if n != -1:
        return -1
    
ans = solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
print("ans : ",ans)