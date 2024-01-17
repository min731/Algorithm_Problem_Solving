def solution(skill, skill_trees):
    answer = len(skill_trees)
    
    for skill_tree in skill_trees:
        skill_set = set(skill)
        tmp = []
        
        for x in skill_tree:
            if x in skill_set:
                tmp.append(x)
                
        tmp = "".join(tmp)
        
        for i in range(len(tmp)):
            if tmp[i]!=skill[i]:
                answer -= 1
                break
            
    return answer