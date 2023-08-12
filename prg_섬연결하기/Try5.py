def solution(n, costs):
    from collections import deque
    import math

    origin_graph = [cost for cost in costs]
    origin_graph = sorted(origin_graph, key=lambda x: x[2],reverse=True)
    origin_graph = deque(origin_graph)

    rotate_cnt = 0
    minium_fee = math.inf

    while rotate_cnt<n:

        print("origin graph : ",origin_graph)

        graph = origin_graph.copy()

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

        if total_fee<minium_fee:
            minium_fee = total_fee

        rotate_cnt += 1

        origin_graph.rotate(1)
        # print("origin graph : ",origin_graph)


    print(minium_fee)
    return minium_fee

solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])