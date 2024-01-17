def solution(skill, skill_trees):
    answer = 0
    # print(set(skill))
    for skill_tree in skill_trees:
        skill_set = set(skill)
        tmp = []
        for x in skill_tree:
            if x in skill_set:
                tmp.append(x)
        # print("tmp : ","".join(tmp), "skill : ",skill)
        tmp = "".join(tmp)
        
        for i in range(1,len(skill)+1):
            if tmp==skill[:i]:
                answer += 1
        # if "".join(tmp)==skill:
        #     answer += 1
            
    return answer