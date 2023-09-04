def solution(n, wires):
    import copy

    answer = -1
    graph = {}
    total = len(wires)

    for wire in wires:
        w1,w2 = map(int,wire)
        
        try:
            graph[w1].append(w2)
        except:
            graph[w1] = []
            graph[w1].append(w2)
        try:
            graph[w2].append(w1)
        except:
            graph[w2] = []
            graph[w2].append(w1)

    print(graph)

    for wire in wires:

        graph2 = copy.deepcopy(graph)
        w1,w2 = map(int,wire)
        graph2[w1].remove(w2)
        graph2[w2].remove(w1)




    return answer

# solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])	
solution(4,[[1,2],[2,3],[3,4]])


def check_edge(graph):

    from collections import deque

    # 시작 1
    queue = deque([1])
    visited = [False for _ in range(len(graph)+1)]

    visited[1] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not (visited[i]):
                queue.append(i)
                visited[i] = True
        print(visited)

    return 

# check_edge({1: [2], 2: [1, 3], 3: [2, 4], 4: [3]})
check_edge({1: [2], 2: [1], 3: [4], 4: [3]})