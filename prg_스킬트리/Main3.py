def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        print("----------------------")
        print("skills : ",skills)
        for s in skills:
            print("s : ",s)
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            # print("else! : ",answer)
            answer += 1
            print("else! : ",answer)

    return answer

solution("CBD",["BACDE", "CBADF", "AECB", "BDA"])