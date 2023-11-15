import re
from collections import deque

def get_format(bin_str,n):
    
    bin_str = deque(bin_str)
    
    print("len(bin_str) : ",len(bin_str))
    print("n : ",n)
    while len(bin_str)!=n:
        bin_str.appendleft("0") 
    
    print("bin_str : ",bin_str)
    
    return "".join(bin_str)
    # return 0

def solution(n, arr1, arr2):
    
    answer = []
    
    for i in range(n):

        
        # print("-----------------------------------")
        # print(bin(arr1[i]))
        #print(bin(arr1[i])!"0"*n)/
        # print(bin(arr2[i]))
        #print(bin(arr2[i])!"0"*n)
        # print(bin(arr1[i]|arr2[i]))
        # print(bin(arr1[i]|arr2[i])[2:])
        
        # print("-----")
        
#         print(get_format(bin(arr1[i])[2:],n))
#         print(get_format(bin(arr2[i])[2:],n))
        
#         line1 = get_format(bin(arr1[i])[2:],n)
#         line2 = get_format(bin(arr2[i])[2:],n)

        x = deque(bin(arr1[i]|arr2[i])[2:])
    
        while len(x) != n:
            x.appendleft("0")
        
        x = "".join(x)
        x = re.sub('1','#',x)
        # print(x)
        x = re.sub('0',' ',x) 
        # print(x)
        
        answer.append(x)
    print(answer)
    return answer