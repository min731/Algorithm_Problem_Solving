def convert_odd(temp):
    ls_temp = list(temp[::-1])
    idx = 0
    for i in ls_temp:
        if i == '1':
            idx += 1
        else :
            break

    ls_temp[idx] = '1'
    ls_temp[idx-1] = '0'
    return int(''.join(ls_temp)[::-1], 2)

def solution(numbers):
    answer=[]
    for number in numbers:
        if number % 2 == 0:
            answer.append(number+1)
        else:
            temp = format(number, 'b')
            if '0' not in temp:
                temp = '0' + temp
            temp = convert_odd(temp)
            answer.append(temp)
    return answer

# print(format(10, 'b'))