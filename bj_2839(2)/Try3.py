N = int(input())

bongji3 = 1

while True:

    sugar = N

    if sugar%5==0:
        print(sugar//5)
        break

    sugar -= bongji3*3

    if sugar<0:
        print(-1)
        break

    if sugar%5 == 0:
        # print("5kg : ",sugar//5," , 3kg : ",bongji3)
        # print("총 갯수 : ",sugar//5+bongji3)
        print(sugar//5+bongji3)
        break
    bongji3 += 1
