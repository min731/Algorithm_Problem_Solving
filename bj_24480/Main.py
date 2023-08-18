from sys import stdin,setrecursionlimit
input = stdin.readline



count = 0
def dfs(graph, visited, start):
    global count
    count+=1
    visited[start] = count
    for i in graph[start]: # 그래프 집합에서
        if visited[i] == False: #방문하지 않은 경우,
            
            dfs(graph, visited, i)


# 입력 #
N, M, R = map(int, input().split())
setrecursionlimit(N+10) # 재귀 깊이 늘리기
#---1번 정점부터 시작한다. --#
# 방문한 곳
visited = [False] * (N+1)
#그래프 ( 정점 집합)
graph = [[]for i in range(N+1)]

# -- 연결하기 -- #
for i in range(M): # 간선의 수 만큼 반복
    u,v = map(int, input().split()) # u,v 입력받기
    graph[u].append(v) # u,v 서로 연결
    graph[v].append(u) # u,v 서로 연결

# -- 내림차순 정렬 -- #
for i in range(1,N+1):
    graph[i].sort(reverse=True)


# -- dfs -- #
dfs(graph, visited, R)


for i in range(1, N+1):
    if visited[i] != False :
        print(visited[i])
    else:
        print(0)