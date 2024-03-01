n = int(input())
a = list(map(int, input().split()))
x = int(input())

answer=0
a.sort()
for i in range(n):
    for j in range(i+1,n):
        if a[i] + a[j] == x:
            answer+=1
        if a[i] + a[j] > x:
            break

print(answer)