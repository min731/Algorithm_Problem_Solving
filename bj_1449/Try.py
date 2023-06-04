N, M = map(int, input().split(" "))

holes = list(map(int, input().split(" ")))
holes.sort()

# print(holes)

ans = 1
loc = holes[0]

for i in range(1, N):
    print("인덱스 : ", i)
    print("현재 위치 : ", loc, " 다음 위치 : ", holes[i])
    if holes[i] < loc + M:
        continue
    print("테이프 추가")
    ans += 1
    loc = holes[i]

print(ans)
