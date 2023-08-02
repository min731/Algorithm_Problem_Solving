from collections import deque

def getData():
    
    N, M, V = list(map(int,input().split()))
    graph = [set()for i in range(N+1)]
    for _ in range(1,M+1): # i= 1~5
        connect = list(map(int,input().split()))
        graph[connect[0]].add(connect[1])
        graph[connect[1]].add(connect[0])

    return graph,V
graph,V = getData()
print(graph)

def DFS(graph,V):
    
    DFS_visited = []
    stack = [V]
    
    while stack:
        n = stack.pop()
        if n not in DFS_visited:
            DFS_visited.append(n)
            stack += sorted(list(graph[n] - set(DFS_visited)),reverse=True) 
    return DFS_visited                                                      
                                                                            
DFS_visited = DFS(graph,V)                                                  

def BFS(graph,V):
    
    BFS_visited = []
    queue = deque([V])
    
    while queue:
        n = queue.popleft()
        if n not in BFS_visited:
            BFS_visited.append(n)
            queue += sorted(graph[n] - set(BFS_visited)) 
    return BFS_visited                           
                                                
BFS_visited = BFS(graph,V)

print(*DFS_visited)
print(*BFS_visited)