T = int(input())

stocks = []

for i in range(T):
    N = int(input())
    stocks.append(list(map(int, input().split(" "))))

for i in range(T):
    buy = []
    ans = 0
    # sorted_stock = stocks[i].sort()
    for j in range(len(stocks[i])):
        if stocks[i][j] < max(stocks[i][j:]):
            buy.append(stocks[i][j])
        else:
            ans += sum(list(map(lambda x: max(stocks[i][j:])-x, buy)))
            buy = []
    print(ans)