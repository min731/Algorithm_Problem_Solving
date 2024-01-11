def find(x):

    if parent[x]!=x:
        return find(parent[x])
    return x

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
    print("--------------------------")
    hap, a,b = map(int,input().split())
    print(hap,a,b)
    if hap==0:
        union(a,b)
        print(parent)
    else:
        if find(a)==find(b):
            print("YES")
        else:
            print("NO")