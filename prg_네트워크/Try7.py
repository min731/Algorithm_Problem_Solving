from collections import deque

def dfs(start,visited,graph):

    cnt = 0
    stack = deque([start])

    while stack:

        node = stack.pop()

        if not visited[node]:
            # stack.extend(graph[node])
            if len(graph[node])==0:
                cnt += 1
            visited[node] = True
    
    return cnt

def solution(n, computers):
    answer = 1

    graph = {i:[] for i in range(1,len(computers[0])+1)}
    # print(graph)

    for i in range(1,len(computers)+1):
        for j in range(1,len(computers[0])+1):
            if i!=j:
                if computers[i-1][j-1]==1:
                    graph[i].append(j)

    stack = deque(graph.keys())
    # stack = deque([1])

    visited = [False for i in range(len(computers[0])+1)]

    while stack:

        node = stack.pop()

        if not visited[node]:
            # stack.extend(graph[node])
            if len(graph[node])==0:
                answer += 1
            visited[node] = True

    return answer 