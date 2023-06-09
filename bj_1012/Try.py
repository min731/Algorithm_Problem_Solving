T = int(input())

farms = []
visited = []

for i in range(T):
    M, N, K = map(int, input().split())

    farms.append([[0] * N for x in range(M)])
    visited.append([[False] * N for x in range(M)])

    for j in range(K):
        x, y = map(int, input().split())

        farms[i][x][y] = 1

# 농장 입력 확인
# for i in range(T):
#     print("----------")
#     for j in range(len(farms[i])):
#         print(farms[i][j])
#         print(visited[i][j])

from collections import deque

# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for t in range(len(farms)):
    length = len(farms[t])
    width = len(farms[t][0])

    print("가로 : ", length,"세로 : ",width)

    ans = 0
    add = 0
    queue = deque([[0, 0]])
    # visited[t][0][0] = True

    if farms[t][0][0] == 1:
        ans = 1

    while queue:

        print("queue : ",queue) 
        v = queue.popleft()
        print("현재 좌표 : ", v[0], v[1])

        visited[t][v[0]][v[1]] = True

        for j in range(len(farms[t])):
        # print(farms[i][j])
            print(visited[t][j])
        
        for i in range(4):
            # print(v[0] + dx[i], v[1] + dy[i])
            if v[0] + dx[i] >= 0 and v[0] + dx[i] < length and v[1] + dy[i] >= 0 and v[1] + dy[i] < width :
                if not visited[t][v[0] + dx[i]][v[1] + dy[i]]:
                    queue.append([v[0] + dx[i], v[1] + dy[i]])
                    # visited[t][v[0] + dx[i]][v[1] + dy[i]] = True


    print(ans)


for i in range(T):
    print("----------")
    for j in range(len(farms[i])):
        # print(farms[i][j])
        print(visited[i][j])