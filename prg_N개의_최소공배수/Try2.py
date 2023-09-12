def min_multi(n1,n2):
    from functools import reduce

    limit = max([n1,n2])
    print("max : ", limit)
    k = 1
    tmp = [1]
    while limit>=k :
        k += 1
        if n1%k==0 and n2%k==0:
            n1/=k
            n2/=k
            tmp.append(k)
    
    print("tmp :",tmp)
    print("최소공배수 : ",int(reduce(lambda x, y: x * y, tmp)*n1*n2))
    return int(reduce(lambda x, y: x * y, tmp)*n1*n2)

def solution(arr):
    from collections import deque

    arr = deque(arr)

    while len(arr)!=1:

        print("--------")
        print("arr : ",arr)
        n1 = arr.popleft()
        n2 = arr.popleft()

        print("n1 : ",n1)
        print("n2 : ",n2)

        arr.appendleft(min_multi(n1,n2))

    print("정답 :",arr[0])
    return arr.pop()


# 2,6,8,14
# 2,2*3,2^3,2*7
# 1,3,2^2,7 1 3 4 7 

solution([14,7,35,2])
# solution([14,6,2,8])
# solution([2,6,8,14])
# solution([1,2,3])
# solution([2,5,10])

# 5 30
# 5 2*3*5
