def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    print(dic)
    print(temp)

    for com in completion:
        temp -= hash(com)
    print(temp)

    answer = dic[temp]

    return answer


solution(["leo", "kiki", "eden"],["eden", "kiki"])