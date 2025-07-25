price = int(input())
zan = 1000-price
cnt = 0

for en in [500,100,50,10,5,1]:
    cnt += zan//en
    # print(f'cnt: {cnt}')
    zan -= en*(zan//en)
    # print(f'zan: {zan}')

print(cnt)

# 380 -> 620 --> 500:1,100:1,10:2