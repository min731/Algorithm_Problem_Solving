import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    command = list(sys.stdin.readline().split())
    todo = command[0] 
    
    if todo == 'push':
        arr.append(command.pop())
    elif todo == 'pop':
        if arr:
            el = arr.pop()
            print(el)
        else:
            print(-1)
    elif todo == 'size':
        print(len(arr))
    elif todo == 'empty':
        if arr:
            print(0)
        else:
            print(1)
    else: # 'top'
        if arr:
            el = arr.pop()
            print(el)
            arr.append(el)
        else:
            print(-1)