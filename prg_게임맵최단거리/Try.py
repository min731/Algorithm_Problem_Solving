def bfs(i,j):

    from collections import deque

    queue = deque([[i,j]])

    while True:

        x,y = queue.popleft()


def solution(maps):

    for i in range(len(maps)):
        print(maps[i])

    global answer
    answer = 0

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            bfs(i,j)

    return answer

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])