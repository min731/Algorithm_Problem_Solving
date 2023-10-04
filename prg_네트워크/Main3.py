def solution(n, computers):            
    
    def DFS(i):
        visited[i] = 1
        for a in range(n):
            print("computers[i][a] : ",computers[i][a])
            if computers[i][a] and not visited[a]:
                DFS(a)      
        print("visited : ",visited)

    answer = 0
    visited = [0 for i in range(len(computers))]
    for i in range(n):
        if not visited[i]:
            DFS(i)
            answer += 1
        
    return answer

solution(3,[[1, 1, 0],[1, 1, 0],[0, 0, 1]]) # 2
# solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]) # 1
# solution(3,[[1, 0, 0], [0, 1, 0], [0, 0, 1]]) # 0