import sys
N=int(input())

stack=[]
for i in range(N):
    order=sys.stdin.readline().split()


    if "push" in order:
        stack.append(order[-1])
    elif "pop" in order:
        if len(stack)==0:
            print(-1)
        else:
            print(stack[len(stack)-1])
            stack.pop(len(stack)-1)
    elif "size" in order:
        print(len(stack))
    elif "empty" in order:
        if len(stack)==0:
            print(1)
        else:print(0)
    elif "top" in order:
        if len(stack)==0:
            print(-1)
        else:print(stack[len(stack)-1])
