def generator(x):

    v = x+sum(list(map(int,str(x))))
    
    return v

tmp = [i for i in range(10001)]
ans = set()

for x in tmp:
    ans.add(generator(x))

self_num = list(set(tmp)-ans)
self_num.sort()

for num in self_num:
    print(num)

