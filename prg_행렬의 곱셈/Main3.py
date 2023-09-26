def productMatrix(A, B):
    answer = []

    for i in range(len(A)):
        arr = []
        for j in range(len(B[0])):
            tmp = 0
            for k in range(len(A[0])):
                tmp += A[i][k] * B[k][j]
            arr.append(tmp)
        answer.append(arr)

    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
a = [ [ 1, 4 ], [ 2, 3 ]]
b = [[1], [2]]
print("결과 : {}".format(productMatrix(a,b)))