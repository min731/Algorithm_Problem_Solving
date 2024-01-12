def find(x):

    if parent[x]!=x:
        parent[x] = find(parent[x])

    return parent[x]

def union(a,b):

    a = find(a)
    b = find(b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
connects = []
parent = [i for i in range(N+1)]
ans = 0

for i in range(1,N+1):
    well = int(input())
    connects.append((well,0,i))

for i in range(1,N+1):
    connect = list(map(int,input().split()))
    for j in range(i+1,N+1):
        connects.append((connect[j-1],i,j))

print(parent)
print(connects)

# cnt = 0
for connect in sorted(connects):
    print("---------------")
    # print(connect)
    cost,a,b = connect
    print(cost,a,b)
    # if connect[1]>0:
    # if cnt==N:
    #     break
    if find(a) != find(b):
        union(a,b)
        print(a,b,"연결")
        print(cost,"추가")
        ans += cost
        # cnt += 1

print(ans)
