T = int(input())

for i in range(T):
    N = int(input())
    stock = list(map(int, input().split()))

    buy = []
    ans = 0
    sorted_stock = sorted(stock)
    for x in stock:
        if x < sorted_stock[-1]:
            buy.append(x)
            sorted_stock.remove(x)
        else:
            ans += sum(sorted_stock[-1]-k for k in buy)
            sorted_stock.pop()
            buy = []
    print(ans)