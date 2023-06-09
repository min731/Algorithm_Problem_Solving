T = int(input())

for i in range(T):
    N = int(input())
    stocks = list(map(int, input().split(" ")))
    act = [stocks[0]]
    ans = 0

    print("---------")

    for j in range(len(stocks) - 1):
        act.append(stocks[j + 1])
        # print(stocks[j + 1 :])
        # print(max(stocks[j + 1 :]))
        if act[-1] >= max(stocks[j + 1 :]):
            print("판매 시점 :", act[-1], stocks[j + 1 :])
            # output2 = list(map(lambda x:x -1, a))
            print(list(map(lambda x: act[-1] - x, act[:-1])))
            ans = ans + sum(list(map(lambda x: act[-1] - x, act[:-1])))
            act = []
            print("현재 값 : ", ans)
    print("최대값 : ", ans)
