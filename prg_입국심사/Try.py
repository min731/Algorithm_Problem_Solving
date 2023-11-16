from bisect import bisect_left

def solution(n, times):
    
    times = sorted(times)
    answer = 0
    audits = []
    
    # for i in range(len(times)):
    #     if i < len(times):
    #         audits.append(times[i])
    #         n -= 1
    #     else:
    #         audits.append(0)

    audits = [0 for i in range(len(times))]
    
    n -= len(audits)
    
    print(audits)
    
#     while n!=0:
        
#         answer += 1
#         audits = [audits+1 for audits in audits]
        
#         for audit in audtis:
            
        
    
    return answer