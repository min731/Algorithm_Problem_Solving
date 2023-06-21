# N,M 크기 입력 받기
N , M = map(int,input().split())

# 캠퍼스
campus = []

# 도연좌표
doyeon = []


for i in range(N):
    tmp = list(input())
    campus.append([])
    for j in range(M):
        if tmp[j] == "I":
            doyeon.append(i)
            doyeon.append(j)
        campus[i].append(tmp[j])

# dfs 구현
stack = [doyeon]

# 초기 좌표 방문
campus[doyeon[0]][doyeon[1]] = 'X'

# 상우하좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]
# 만난 친구 수
cnt = 0

while stack:

    v = stack.pop()

    if campus[v[0]][v[1]] == 'P':
        cnt += 1

    campus[v[0]][v[1]] = 'X'

    for i in range(4):
        
        newX = v[0] + dx[i]
        newY = v[1] + dy[i]

        if newX >=0 and newX < N and newY >= 0 and newY < M:
            if campus[newX][newY] != 'X':
                stack.append([newX,newY])

if cnt > 0 :
    print(cnt)
else:
    print("TT")


# def test(x):

#     return ['TT',x] [x>0]

# x = 1
# y = test(x)
# print(y)
