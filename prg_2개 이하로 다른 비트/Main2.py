def get_bin(x):
    x = bin(x)[2:]
    
    return x

def solution(numbers):
    answer = []
    
    for num in numbers:
        # num = get_bin(num)
    
        if num%2==0:
            num = get_bin(num)
            num = num[:-1] + '1'
            answer.append(int(num,2))
            
        else:
            num = get_bin(num)
            num = '0'+num
            idx = num.rindex('0')
            num = num[:idx]+'10'+num[idx+2:]
            answer.append(int(num,2))
    
    return answer