def solution(gems):
    answer = []
    
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
            answer.append([start+1,end+1,end-start+1])
            start += 1
        elif buy<kinds:
            end += 1
        
        # elif buy>kinds:
        #     start += 1
    
    answer = sorted(answer, key = lambda x : (x[2],x[0]))
    # print(answer)
    answer = answer[0][:2]
    # print(answer)
    
    return answer