def solution(arr, divisor):
    ans = sorted([a for a in arr if a%divisor == 0])  
    return ans if len(ans)!=0 else [-1]