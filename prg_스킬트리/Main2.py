def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        skill_set = set(skill)
        tmp = []
        
        for x in skill_tree:
            if x in skill_set:
                tmp.append(x)
                
        tmp = "".join(tmp)
        
        for i in range(0,len(skill)+1):
            if tmp==skill[:i]:
                answer += 1
                break
            
    return answer