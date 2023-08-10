N = int(input())
times = list(map(int,input().split()))
print(times)

times.sort()
print(times)

total = 0
now = 0

for time in times:
    now += time
    total += now
print(total)