N, M, V = map(int,input().split())
# print(N,M,V)

graph = {str(i):[] for i in range(1,N+1)}
# print(graph)

for i in range(M):
    k,v = input().split()
    graph[k].append(int(v))

print(graph)
visited = [False for _ in range(N)]

def dfs(graph,target):

    # visited = [False for _ in range(N)]
    print(target)
    while True:

        values = graph[target]
        values.sort()

        for v in values:

            if not visited[v-1]:

                target = str(v)
                visited[v-1] = True
                # print("target : ",target)
                dfs(graph,target)
        break

dfs(graph,str(V))

        
        
