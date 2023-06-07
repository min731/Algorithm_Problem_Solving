T = int(input())

ansList = []
stocks = []

for i in range(T):
    N = int(input())
    stocks.append(list(map(int, input().split(" "))))

for i in range(T):
    
    act = [stocks[i][0]]
    ans = 0

    for j in range(len(stocks[i]) - 1):
        act.append(stocks[i][j + 1])

        if act[-1] >= max(stocks[i][j + 1 :]):
            ans = ans + sum(list(map(lambda x: act[-1]-x, act[:-1])))
            act = []
    
    if ans < 0 :
        ans = 0
    ansList.append(ans)

for i in range(T):
    print(ansList[i])
