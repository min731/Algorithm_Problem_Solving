def solution(numbers):
    answer = ''
    length = sum([len(str(num)) for num in numbers])
    # answer += length*'0'
    print(answer)

    while length>0:

        tmp = '0'
        for num in numbers:
            if tmp < answer+str(num)+(length-len(str(num)))*'0':
                find_num = num
                tmp = answer+str(num)
                # del_num = len(str(num))
                # break

        answer = answer+str(find_num)
        del_num = len(str(find_num))
        numbers.remove(find_num)
        length -= del_num

    print(answer)
    return  answer

# solution([6, 10, 2])
# solution([3, 30, 34, 5, 9])
solution([9,997])