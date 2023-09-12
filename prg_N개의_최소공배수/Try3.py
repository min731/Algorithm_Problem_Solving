def solution(arr):
    from functools import reduce
    
    k = 2
    tmp = []
    while max(arr)>k:

        print("k : ",k)
        c_divisor = True
        for el in arr:
            if el%k!=0:
                c_divisor = False
                break
        
        print("c_divisor : ",c_divisor)
        if c_divisor:
            tmp.append(k)
            arr = [int(i/k) for i in arr]

        k += 1
            
    print(arr)
    print(tmp)

    # print("정답 : ",reduce(lambda x, y: x * y, tmp)*reduce(lambda x, y: x * y, arr))
    # return reduce(lambda x, y: x * y, tmp)*reduce(lambda x, y: x * y, arr)


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
