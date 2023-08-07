N = int(input())
M = int(input())

graph = { str(i+1):[] for i in range(N)}
visited = [False for _ in range(N+1)]
visited[0] = True
visited[1] = True

for _ in range(M):
    k,v = map(int,input().split())
    # 양방향
    graph[str(k)].append(v)
    graph[str(v)].append(k)

# 시작점
stack = ['1']

cnt = 0
while stack:
  
    v = stack.pop()

    for x in graph[v]: 
        if not visited[int(x)]:
            visited[int(x)] = True
            # 탐색하지 않은 노드 append
            stack.append(str(x))
            cnt += 1

    # 탐색한 노드 초기화
    graph[v] = []

print(cnt)