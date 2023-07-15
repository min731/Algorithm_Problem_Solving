T = int(input())

stacks = []
for i in range(T):
    stacks.append(list(input()))

for stack in stacks:
    tmp = 0
    is_No = False

    while stack:

        v = stack.pop()
        if v == ')':
            tmp += 1
        else:
            tmp -= 1

        if tmp < 0:
            is_No = True
            break

    if tmp != 0:
        print("NO")
    elif is_No:
        print("NO")
    elif tmp == 0:
        print("YES")