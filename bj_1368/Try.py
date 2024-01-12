N = int(input())
wells = {}
connects = {}

for i in range(N):
    wells[i] = int(input())

for i in range(N):
    connect = map(int,input().split())
    connects[i] = {}
    for j,con in enumerate(connect):
        connects[i][j] = con

# print(wells)
# print(connects)
        
