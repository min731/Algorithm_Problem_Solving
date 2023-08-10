N = int(input())
times = list(map(int,input().split()))
print(times)

# times.sort()

print(times)
import itertools
import math

minium = math.inf
for case in itertools.permutations(times, len(times)):
    
    case = list(case)
    print(case)

    now = 0
    total = 0

    while case:
        v0 = case.pop()
        now += v0
        total += now
    
    if total<minium:
        minium=total

print(minium)