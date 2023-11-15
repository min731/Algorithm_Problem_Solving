import re
from collections import deque

def get_format(bin_str,n):
    
    bin_str = deque(bin_str)

    while len(bin_str)!=n:
        bin_str.appendleft("0") 
    return "".join(bin_str)

def solution(n, arr1, arr2):
    
    answer = []
    
    for i in range(n):

        x = deque(bin(arr1[i]|arr2[i])[2:])
    
        while len(x) != n:
            x.appendleft("0")
        
        x = "".join(x)
        x = re.sub('1','#',x)
        x = re.sub('0',' ',x) 
        
        answer.append(x)
    return answer