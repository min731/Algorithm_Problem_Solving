def solution(n, left, right):
    from collections import deque

    arr = deque([])

    for i in range(1,n+1):
        print("--------------")
        for j in range(i,n+1):
            if i==j:
                for k in range(1,i+1):
                    arr.append(j)
            else:
                arr.append(j)
            print("i,j : ",i,j)
            print("arr : ",arr)

    print(arr)

    answer = []
    return answer

solution(3,2,5)
solution(4,7,14)