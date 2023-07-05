n = int(input())

stu = {}

for _ in range(n):
    birth = []
    info = input().split()
    print(info)
    stu[info[0]] = info[1:]

print(stu)
values = []

for value in stu.values():
    values.append(value)

values.sort(key=lambda x:(x[0],x[1],x[2]))

print(values)


# values = sorted(values)
# print(values)


for key,value in stu.items():
    if value == values[0]:
        print(key)
    if value == values[len(values)-1]:
        print(key)

# print()