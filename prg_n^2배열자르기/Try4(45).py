def solution(n, left, right):
    answer = 0

    arr = []
    cnt = 0
    can_stop = False
    for i in range(n):
        tmp = []
        for j in range(n):

            if cnt>=right+1:
                can_stop = True
                arr.extend(tmp)
                break
            if i+1>=j+1:
                tmp.append(i+1)
            else:
                tmp.append(j+1)
            cnt += 1
        if can_stop:
            print("cnt : ",cnt)
            # arr.append(tmp)
            break

        arr.extend(tmp)
    print(arr)
    print(arr[left:right+1])
    # print(answer)
    return arr[left:right+1]

# solution(3,2,5)
solution(4,7,14)