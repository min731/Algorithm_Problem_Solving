def find(x):

    if parent[x]!=x:
        parent[x] = find(parent[x])
        # return find(parent[x])
    return parent[x]
    # return x

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a<b:
        parent[b]=a
    else:
        parent[a]=b


n,m = map(int,input().split())
# print(n,m)
parent = {i:i for i in range(n+1)}

check = []
for _ in range(m):
    hap, a,b = map(int,input().split())
    check.append((hap,a,b))

for case in check:
    print("--------------------------")
    hap, a,b = case
    print(hap,a,b)
    if hap==0:
        union(a,b)
        print(parent)
    else:
        if find(a)==find(b):
            print("YES")
        else:
            print("NO")