def bitwise_xor_list(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

def solution(data, col, row_begin, row_end):
    answer = []

    data = sorted(data, key=lambda x: (x[col-1],-x[0]))

    print(data)
    
    n = len(data[0])

    for i in range(row_begin,row_end+1):
        tmp = data[i-1]
        print("tmp : ",tmp)
        v = 0
        for j in range(n):
            print(" tmp[j] 나머지 i : ",tmp[j],i, " => ",tmp[j]%i )
            v += tmp[j]%i
        answer.append(v)

    result = bitwise_xor_list(answer)
    print(result)
    return result

solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]],2,2,3)