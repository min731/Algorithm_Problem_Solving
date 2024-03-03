def change(empty,a,b):
    
    value, reminder = divmod(empty,a)
    new = (value)*b
    
    return new,reminder

def solution(a, b, n):
    answer = 0
    
    while n>=a:
        
        new, reminder = change(n,a,b)
        answer += new
        n = new+reminder
        
    return answer