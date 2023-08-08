N = int(input())

if N%5 == 0:
    print(N/5)
elif N%3 == 0:
    print(N/3)
else:

    bongji3 = 1
    loop = N//5

    # loop=3
    while True:
        
        sugar = N
        sugar -= bongji3*3

        if sugar%5 == 0:
            print("5kg : ",sugar//5," , 3kg : ",bongji3)
            print("총 갯수 : ",sugar//5+bongji3)
            break
        bongji3 += 1
