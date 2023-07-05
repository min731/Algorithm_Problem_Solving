word = str(input())
check = {}

for el in word:
    if el.upper() not in check.keys():
        check[el.upper()] = 0
    check[el.upper()] += 1

most = []
max = max(check.values())

for key,value in check.items():
    if check[key] == max:
        most.append(key) 

if len(most) == 1:
    print(most[0])
else:
    print('?')