def solution(gems):
    answer = [-1,-1,len(gems)+1]
    
    # ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    #    1      2       3       4      5        6           7        8
    
    kinds = len(set(gems))
    # print(kinds)
    start = 0
    end = 0
    
    while end <= len(gems)+1:
        
        buy = len(set(gems[start:end+1]))
        
        # print("start : ",start, "end : ",end, "buy : ",buy)
        
        if buy==kinds:
            # print("start : ",start, "end : ",end, "buy : ",buy)
            now_len = end-start+1 
            if now_len<answer[2]:
                answer = [start+1,end+1,now_len]
                if now_len==kinds:
                    break
            start += 1
            
        elif buy<kinds:
            end += 1
            
    answer = answer[:2]
    
    return answer