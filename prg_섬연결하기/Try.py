def solution(n, costs):
    answer = 0
    
    graph = [cost for cost in costs]
    visitied = [False for _ in range(n)]

    visitied[graph[-1][0]] = True
    total_fee = 0

    stop_list = [graph[-1][0]]

    while graph:

        print("graph : ",graph)
        print("visited : ",visitied)

        go,stop,fee = graph.pop()

        if not visitied[stop] and visitied[go]:
            visitied[stop] = True
            stop_list.append(stop)
            total_fee += fee
        elif not visitied[go] and visitied[stop]:
            visitied[go] = True
            stop_list.append(go)
            total_fee += fee
        print("stop_list : ",stop_list)
        print("total_fee : ",total_fee)

    print("---------------------")
    print("stop_list : ",stop_list)
    print("total_fee : ",total_fee)
    return answer

solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])