N = int(input())
nArray = set(map(int, input().split()))
M = int(input())
mArray = list(map(int, input().split()))

for i in range(M):
    if mArray[i] in nArray:
        print("1")
    else:
        print("0")