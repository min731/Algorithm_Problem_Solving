N, M = map(int,input().split(' '))

# brands = [[-1,-1] for i in range(M)]
# print(brands)

pack = []
piece = []

cases = []

for i in range(M):
    tmp = list(map(int,input().split(' ')))
    # print(tmp)
    pack.append(tmp[0]) 
    piece.append(tmp[1])

if N%6 == 0:
    cases.append(min(pack)*(N//6))
    cases.append(min(piece)*N)
else:
    # print(min(pack)*(N//6),min(piece)*(N%6))
    cases.append(min(pack)*(N//6)+min(piece)*(N%6))
    cases.append(min(pack)*(N//6+1))
    cases.append(min(piece)*N)

# print(cases)
print(min(cases))


# print(brands)

