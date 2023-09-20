def solution(n, left, right):
    from collections import deque

    arr = deque([])
    can_stop = False

    for i in range(1,n+1):
        print("--------------")
        for j in range(i,n+1):
            if i==j:
                for k in range(1,i+1):
                    arr.append(j)
            else:
                arr.append(j)

            if len(arr)>=right+1:
                can_stop=True
                break
        if can_stop:
            break

    print(arr)

    answer = list(arr)[left:right+1]
    print(answer)
    return answer

# solution(3,2,5)
solution(4,7,14)