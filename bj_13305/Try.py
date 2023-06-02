N = int(input())

distance = list(map(int, input().split()))
n_distance = len(distance)

price = list(map(int, input().split()))
n_price = len(price)

total_distance = sum(distance)
min_price = price[0] * total_distance
import itertools

permu = [i for i in range(total_distance + 1)]
print([permu] * n_distance)

print(permu)
for case in itertools.product(permu, permu, permu):
    flag = True
    prices = 0
    for i in range(n_distance):
        if sum(case[0:i]) < sum(distance[0:i]):
            flag = False
            break
    if flag:
        if sum(case) == total_distance:
            print(case)
            for i in range(n_distance):
                prices += case[i] * price[i]
            print(prices)
            if min_price > prices:
                min_price = prices

print(min_price)
