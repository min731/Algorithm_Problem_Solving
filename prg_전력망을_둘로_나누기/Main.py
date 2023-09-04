def check_edge(graph):

    from collections import deque

    # 시작 1
    queue = deque([1])
    visited = [0 for _ in range(len(graph)+1)]
    
    visited[1] = 1

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not (visited[i]):
                queue.append(i)
                visited[i] = 1

    for idx,visit in enumerate(visited):
        if visit==0:
            visited[idx] = -1

    visited[0] = 0

    return sum(visited)

def solution(n, wires):
    import copy

    answer = len(wires)
    graph = {}

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

    for wire in wires:

        graph2 = copy.deepcopy(graph)
        w1,w2 = map(int,wire)
        graph2[w1].remove(w2)
        graph2[w2].remove(w1)

        tmp = check_edge(graph2)

        if abs(tmp) < answer:
            answer = abs(tmp)

    return answer

# solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])	
# solution(4,[[1,2],[2,3],[3,4]])
solution(7,[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]])