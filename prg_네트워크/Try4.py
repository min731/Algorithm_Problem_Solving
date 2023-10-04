from collections import deque

def solution(n, computers):
    answer = 0

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
        print("stack : ",stack)
        node = stack.pop()
        print("node : ",node)
        print("graph : ",graph)
        if not visited[node]:
            # stack.extend(graph[node])
            if graph[node] == []:
                answer += 1
            # else:
            #     graph[node].pop()
            visited[node] = True
        print("visited: ",visited)

    print("answer :",answer)
    return answer 

solution(3,[[1, 1, 0],[1, 1, 0],[0, 0, 1]]) # 2
# solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]) # 1
# solution(3,[[1, 0, 0], [0, 1, 0], [0, 0, 1]]) # 0