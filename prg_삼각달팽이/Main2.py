def solution(n):
    res = [[0] * n for _ in range(n)]   # 모두 0으로 개수만큼 세팅
    answer = []
    x, y = -1, 0        # for문 실행시 x값을 처음에 0으로 세팅해주기 위해 초기값은 -1로 세팅
    num = 1             # 들어갈 숫자

    for i in range(n):
        for j in range(i, n):
            # down
            if i % 3 == 0:          # 3으로 퍼센트연산해준 이유는 down/right/up 세 동작이기 때문
                x += 1

            # right
            elif i % 3 == 1:
                y += 1

            # up
            elif i % 3 == 2:
                x -= 1
                y -= 1

            res[x][y] = num        # res에 저장
            num += 1

    for i in res:
        for j in i:
            if j != 0:
                answer.append(j)   # 저장했던 배열 for문이용 합쳐줍니다.

    return answer

print(sum([[1,0],[2,3]],[]))