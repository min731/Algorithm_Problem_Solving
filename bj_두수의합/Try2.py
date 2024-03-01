n = int(input())
arr = list(map(int,input().split()))
x = int(input())
ans = 0

arr.sort()
print("arr : ",arr)

front = 0
rear = len(arr)-1

while front<rear:

    print("front : ",front," rear : ",rear)
    tmp = arr[front]+arr[rear]
    print("tmp : ",tmp)

    if tmp==x:
        ans += 1
        rear -= 1
    elif tmp<x:
        front += 1
    else:
        rear -= 1

print(ans)