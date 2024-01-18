def solution(gems):
    answer = [1,len(gems),len(gems)]
    
    kinds = len(set(gems))

    start,end = 0,0
    buy = {gems[0]:1}
    
    while start<len(gems) or end<len(gems):
        
        if len(buy.keys())==kinds:
            # print("start : ",start, "end : ",end, "buy : ",buy)
            now_len = end-start+1
            
            if now_len<answer[2]:
                answer = [start+1,end+1,now_len]
                if now_len==kinds:
                    break
            if buy[gems[start]]==1:
                del buy[gems[start]]
                # buy[gems[start]] -= 1
            else:
                # del buy[gems[start]]
                buy[gems[start]] -= 1
                
            start += 1
            
        elif len(buy.keys())<kinds:
            end += 1
            if end==len(gems):
                break
            buy[gems[end]] = buy.get(gems[end],0) + 1
            # end += 1
            
    answer = answer[:2]
    return answer

# solution(["AA", "AB", "AC", "AA", "AC"])
solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
# solution(['A','B', 'B', 'B', 'C', 'D','D', 'D','D' ,'D', 'D' ,'B', 'C' ,'A']) # 12:15

# solution(['DIA', 'EM', 'EM', 'RUB', 'DIA']) # answer = [3, 5] output = [1, 4]