N, M = map(int,input().split(' '))

brands = [[-1,-1] for i in range(M)]
# print(brands)

cases = []

for i in range(M):
    tmp = list(map(int,input().split(' ')))
    # print(tmp)
    brands[i][0] = tmp[0] 
    brands[i][1] = tmp[1]

for i in range(0,N//6+2):
    print(N//6+1)
    for j in range(M):
        print(i*6,N%6)
        cases.append(brands[j][0]*i*6 + brands[j][1]*(N%6))

print(cases)


# print(brands)

