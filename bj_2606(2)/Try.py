N = int(input())
M = int(input())

graph = { str(i+1):[] for i in range(N)}
visited = [False for _ in range(N+1)]
visited[0] = True
visited[1] = True

# print(graph)
print(visited)

for _ in range(M):
    k,v = map(int,input().split())
    graph[str(k)].append(v)
    graph[str(v)].append(k)

print(graph)

stack = ['1']

cnt = 0
while stack:
    
    print("---------------")
    print("stack : ",stack)
    v = stack.pop()

    print("v : ",v)

    for x in graph[v]: 
        if not visited[int(x)]:
            visited[int(x)] = True
            stack.append(str(x))
            cnt += 1

    graph[v] = []

print(cnt)