n = int(input())
time_list = list(map(int, input().split()))
time_list.sort()

for i in range(1, n):
    time_list[i] += time_list[i-1]
    
print(sum(time_list))