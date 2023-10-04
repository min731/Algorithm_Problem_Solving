from collections import deque

def dfs(start,graph,visited,answer):

    stack = deque([start])

    while stack:

        node = stack.pop()

        if not visited[node]:
            stack.extend(graph[node])
            visited[node] = True

    answer += 1
    return answer,visited
    

def solution(n, computers):
    answer = 0

    graph = {i:[] for i in range(1,len(computers[0])+1)}

    for i in range(1,len(computers)+1):
        for j in range(1,len(computers[0])+1):
            if i!=j:
                if computers[i-1][j-1]==1:
                    graph[i].append(j)
    
    visited = [False for i in range(len(computers[0])+1)]

    for i in range(1,n+1):
        if not visited[i]: 
            answer,visited = dfs(i,graph,visited,answer)

    return answer 