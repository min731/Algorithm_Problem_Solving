def find(x):

    value = parent[x]
    while value!=x:
        # parent[x] = value
        x = value
        value = parent[value]
    return value

def union(a,b):
    origin_a = a
    origin_b = b
    a = find(a)
    b = find(b)
    
    if a<b:
        parent[origin_b]=a
    else:
        parent[origin_a]=b


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