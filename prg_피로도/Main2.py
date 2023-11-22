answer = 0
N = 0
visited = []

def dfs(k, cnt, dungeons):
    print("visited : ",visited)
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):

        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            # print("visited : ",visited)
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            # print("visited : ",visited)
            visited[j] = 0
            # print("------")
            # print("visited : ",visited)

def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer

solution(80,[[80,20],[50,40],[30,10]])


print([1]+[2])