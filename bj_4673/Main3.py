nature_num = set(range(1,10001))
numList = set()

for i in nature_num:
    for j in str(i):
        i += int(j)
    numList.add(i)
    
self_num = sorted(nature_num - numList)
# print(type(self_num)) #list
for i in self_num:
    print(i)