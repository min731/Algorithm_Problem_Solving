def solution(n, computers):
    answer = 0

    graph = {i:[] for i in range(len(computers[0]))}
    # print(graph)

    for connect in computers:
        pair = []
        for idx,com in enumerate(connect):
            if com==1:
                pair.append(idx)
        graph[pair[0]].append(pair[1])
        graph[pair[1]].append(pair[0])
    
    print(graph)
    return answer 

solution(3,[[1, 1, 0],[1, 1, 0],[0, 0, 1]])