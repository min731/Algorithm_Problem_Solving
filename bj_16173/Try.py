N = int(input())

graph = [[] for _ in range(N)]

# print(graph)

for i in range(N):
    line = list(map(int, input().split()))
    graph[i] = line

vistied = [[False] * N for _ in range(N)]
# print(vistied)

from collections import deque

queue = deque([[0, 0]])
# print(queue)

while queue:
    # print("큐 : ", queue)
    v = queue.popleft()
    # print("현재 위치 : ", v[0], v[1])
    if graph[v[0]][v[1]] == -1:
        print("HaruHaru")
        break
    add = graph[v[0]][v[1]]
    # print("add : ", add)

    if not vistied[v[0]][v[1]]:
        # 하

        if v[1] + add <= N - 1:
            queue.append([v[0], v[1] + add])

        # 우
        if v[0] + add <= N - 1:
            queue.append([v[0] + add, v[1]])

        vistied[v[0]][v[1]] = True

    if len(queue) == 0:
        print("Hing")
        break
