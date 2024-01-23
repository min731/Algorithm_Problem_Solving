n, k = map(int, input().split())
array = list(map(int, input().split()))
psum = [0] * (n+1)
s = 0

for i in range(n):
    s += array[i]
    psum[i+1] = s

ans = -int(1e9)

for i in range(k, n+1):
    ans = max(ans, psum[i]-psum[i-k])
print(ans)