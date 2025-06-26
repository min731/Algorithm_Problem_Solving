def solution(brown, yellow):
    
    total = brown+yellow
    x,y = 0,0
    
    for i in range(1,total+1):
        if total%i==0:
            x = total/i
            y = total/x
            
            if 2*y + 2*(x-2) == brown:
                break
    
    return x,y