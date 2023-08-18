N, M, R = map(int,input().split())
# print(N,M,R)

graph = {i+1:[] for i in range(N)}
print(graph)

for _ in range(M):
    start,end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

# print(graph)

stack = [R]
visited = [False for _ in range(N+1)]
visited[R] = True
print(R)
order = [0 for _ in range(N)]
order[0] = R
cnt = 1

while stack:

    v = stack.pop()
    # [1,2,3]
    graph[v].sort()
    nexts = graph[v]

    for next in nexts:
        v1 = graph[next].pop()
        if not visited[v1]:
            print(v1)
            order[cnt] = v1
            cnt += 1
            stack.append(v1)
            visited[v1] = True
    # print("visited :",visited)

print("---------------")
for ord in order:
    print(ord)