def bitwise_xor_list(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

def solution(data, col, row_begin, row_end):
    answer = []

    data = sorted(data, key=lambda x: (x[col-1],-x[0]))

    
    n = len(data[0])

    for i in range(row_begin,row_end+1):
        tmp = data[i-1]

        v = 0
        for j in range(n):

            v += tmp[j]%i
        answer.append(v)

    result = bitwise_xor_list(answer)

    return result