T = int(input())

stacks = []
for i in range(T):
    stacks.append(list(input()))

for stack in stacks:
    print("----------")
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
            print("No")
            break

    if tmp == 0:
        print("Yes")
    elif not is_No and tmp !=0:
        print("No")