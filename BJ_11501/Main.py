T = int(input())

ansList = []

for i in range(T):
    N = int(input())
    stocks = list(map(int, input().split(" ")))
    act = [stocks[0]]
    ans = 0

    for j in range(len(stocks) - 1):
        act.append(stocks[j + 1])

        if act[-1] >= max(stocks[j + 1 :]):
            ans = ans + sum(list(map(lambda x: act[-1]-x, act[:-1])))
            act = []
        
    if ans < 0 :
        ans = 0
    ansList.append(ans)

for i in range(T):
    print(ansList[i])
