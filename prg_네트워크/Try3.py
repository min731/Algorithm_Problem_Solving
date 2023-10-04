from collections import deque

def solution(n, computers):
    answer = 1

    graph = {i:[] for i in range(1,len(computers[0])+1)}
    # print(graph)

    for i in range(1,len(computers)+1):
        for j in range(1,len(computers[0])+1):
            if i!=j:
                if computers[i-1][j-1]==1:
                    graph[i].append(j)
    print(graph)

    stack = deque(graph.keys())
    # stack = deque([1])
    print(stack)
    visited = [False for i in range(len(computers[0])+1)]
    print(visited)

    while stack:

        print("----------------------")
        node = stack.pop()
        print("node : ",node)
        print("graph[node] : ",graph[node])
        if not visited[node]:
            # stack.extend(graph[node])
            if len(graph[node])==0:
                answer += 1
            visited[node] = True
        print(visited)

    print("answer :",answer)
    return answer 

# solution(3,[[1, 1, 0],[1, 1, 0],[0, 0, 1]])
solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]])