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
    visited[t][0][0] = True
    last_v = [0,0]
    ans_list = []

    if farms[t][0][0] == 1:
        ans_list.append([0,0])

    while queue:

        print("queue : ",queue) 
        v = queue.popleft()
        print("현재 좌표 : ", v[0], v[1])
        
        for i in range(4):
            if v[0] + dx[i] >= 0 and v[0] + dx[i] < length and v[1] + dy[i] >= 0 and v[1] + dy[i] < width :
                if not visited[t][v[0] + dx[i]][v[1] + dy[i]]:
                    if farms[t][v[0] + dx[i]][v[1] + dy[i]] == 1:
                        queue.appendleft([v[0] + dx[i], v[1] + dy[i]])
                        ans_list.append([v[0] + dx[i], v[1] + dy[i]])
                    else:
                        queue.append([v[0] + dx[i], v[1] + dy[i]])
                    visited[t][v[0] + dx[i]][v[1] + dy[i]] = True

        last_v = v

    last_x0 = ans_list[0][0]
    last_x1 = ans_list[0][1]

    if len(ans_list) == 1:
        ans = 1
        print(ans)
        break

    ans_list = sorted(ans_list)

    for idx,x in enumerate(ans_list):
        # if idx == 0:
        #     ans = 1
        if idx == len(ans_list)-1:
            break
        if (abs(ans_list[idx][0] - ans_list[idx+1][0]) == 1 and ans_list[idx][1] - ans_list[idx+1][1] == 0) or (ans_list[idx][0] - ans_list[idx+1][0] == 0 and abs(ans_list[idx][1] - ans_list[idx+1][1]) == 1) :
            continue
        print()
        print("ans 추가 : ", idx,x)
        ans += 1

    print(ans_list)
    print(ans)


# for i in range(T):
#     print("----------")
#     for j in range(len(farms[i])):
#         # print(farms[i][j])
#         print(visited[i][j])