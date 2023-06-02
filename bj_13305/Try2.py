N = int(input())

distance = list(map(int, input().split()))
n_distance = len(distance)

price = list(map(int, input().split()))
n_price = len(price)

total_distance = sum(distance)
min_price = price[0] * total_distance

for i in range(total_distance + 1):
    for j in range(total_distance + 1):
        for k in range(total_distance + 1):
            prices = 0
            if i + j + k == 6:
                print(i, j, k)
                for n in range(n_distance):
                    # print(i, j, k)
                    print(distance[n], price[n])
                    prices += distance[n] * price[n]
                print(prices)
                if min_price > prices:
                    min_price = prices
print(min_price)
