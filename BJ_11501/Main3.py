T = int(input())

stocks = []

for i in range(T):
    N = int(input())
    stocks.append(list(map(int, input().split(" "))))

for i in range(T):
    buy = []
    ans = 0
    print("--------")
    for j in range(len(stocks[i])):
        print(j)
        print(stocks[i][j+1:])
        # print("구매한 주식 : ",act,"  그 뒤 주식", stocks[i][j+1:])
        if stocks[i][j] < max(stocks[i][j:]):
            buy.append(stocks[i][j])
        else:
            ans += sum(list(map(lambda x: max(stocks[i][j:])-x, buy)))
            buy = []
        print("구매한 주식 : ", buy)
    print("최댓값 :",ans)