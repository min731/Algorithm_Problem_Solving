N = int(input())
ropes = []

for i in range(N):
    ropes.append(int(input()))

ropes.sort()

max = 0

for i in range(len(ropes)):
    if max < ropes[i] * (len(ropes) - i):
        max = ropes[i] * (len(ropes) - i)
print(max)
