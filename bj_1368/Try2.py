def find(x):

    x = int(x)
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
connects = {} # {'00':5}
parent = {i:i for i in range(N)} # {0:0}
ans = 0

for i in range(N):
    connects[str(i)+str(i)] = int(input()) # {'00':2}
ans += min(connects.values())

for i in range(N):
    connect = map(int,input().split())
    for j,con in enumerate(connect):
        if con>0:
            connects[str(i)+str(j)] = con # {'01':2}

print(parent)
print(connects)

for connect in sorted(connects.items(),key= lambda x : x[1]):
    print("---------------")
    # print(connect)
    # ('01', 2)
    a,b = connect[0]
    print(a,b)
    # if connect[1]>0:
    if find(a) != find(b):
        union(a,b)
        print(a,b,"연결")
        print(connects[connect[0]],"추가")
        ans += connects[connect[0]]

print(ans)
