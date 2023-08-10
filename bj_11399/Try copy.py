N = int(input())
times = list(map(int,input().split()))
print(times)

# times.sort()

print(times)
import itertools
import math

minium = 0
now_x = 0
for x in times:
    now_x += x
    minium += now_x

for case in itertools.permutations(times, len(times)):
    
    case = list(case)
    print(case)

    now = 0
    total = 0

    while case:
        v = case.pop()
        now += v
        print("-----")
        print(v)
        total += now
        print(now)
        print(total)
        print("-----")

        if total>minium:
            break
    
    if total<minium:
        minium=total

print(minium)