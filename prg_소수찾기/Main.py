from itertools import permutations,product

def is_prime(num):
    
    if num in [0,1]:
        return False
    
    for i in range(2,num):
        if num%i==0:
            return False
        
    return True

def solution(numbers):
    answer = 0
    
    nums = list(numbers)
    case = []
    
    for i in range(1,len(nums)+1):
        tmp = list(permutations(nums,i))
        # print(tmp)
        for j in range(len(tmp)):
            st = ""
            for k in range(len(tmp[j])):
                st += tmp[j][k]
            tmp[j] = int(st)
        tmp = list(set(tmp))
        case.extend(tmp)
                         
    case = list(set(case))
    
    for x in case:
        print(x)
        if is_prime(x):
            # print(x)
            answer += 1
    
    return answer