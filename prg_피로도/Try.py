# from itertools import combinations
from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    for case in permutations(dungeons,len(dungeons)):
        
        # print("---------------------------")
        now = [k,0]
        # print(case)
        for dungeon in case:
            
            required = dungeon[0]
            used = dungeon[1]
            
            if required<=now[0]:
                now[0] -=used
                now[1] += 1
                
            # print("required : ",required)
            # print("used : ",used)
            # print("now : ",now)
                
        if answer<now[1]:
            answer = now[1]
        
    return answer