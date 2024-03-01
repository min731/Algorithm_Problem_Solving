n = int(input())
arr = list(map(int,input().split()))
x = int(input())
ans = 0

arr.sort()
arr += [0]

front = 0
rear = 1

while front<rear and rear<=len(arr)-1:

    print("front : ",front," rear : ",rear)
    tmp = sum(arr[front:rear+1])
    print("tmp : ",tmp)

    if tmp==x:
        ans += 1
    elif tmp<x:
        rear += 1
    else:
        front += 1

print(ans)