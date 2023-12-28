def k_jinsoo(k,n):
    
    now = 0
    m = 0  
    
    while now<=n:
        now *= k
        print(now)
        m += 1
    
    print(m)
        
def solution(n, k):
    answer = -1
    
    k_jinsoo(k,n)
    
    return answer

solution(110011,10)