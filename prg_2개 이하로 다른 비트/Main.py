def get_bin(x):

    x = bin(x)[2:]
    # length = len(x)
    # x = '0'*(length%4)+x   
    
    return x

def solution(numbers):
    answer = []
    
#     print(bin(16))
#     print(bin(32))
    
    
    for num in numbers:

        # print(bin(num))
        bigger =  num+1
        
        num = get_bin(num)
        # print(num)
        # bigger =  num+1
        find = False
        
        while not find:
            
            diff = 0
            bigger_bin = get_bin(bigger)               
            
            # print("num : ",num, "bigger_bin :",bigger_bin)
            
            
            if len(bigger_bin)>len(num):
                num = '0'*(len(bigger_bin)-len(num)) + num
            
            # print("num : ",num, "bigger_bin :",bigger_bin)
                        
            for x1,x2 in zip(num,bigger_bin):
                if x1!=x2:
                    diff += 1
                if diff>=3:
                    break
                           
            if diff<=2:
                answer.append(bigger)
                break

            bigger += 1
            
        # print(bin(num))
    return answer