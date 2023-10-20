def solution(s):
    answer = []
    
    s = s.lstrip('{')
    print(s)
    s = s.rstrip('}')
    print(s)

    s = s.split('},{')
    print(s)

    # print(s[1].split(','))

    new_s = []
    for i in s:
        print(i.split(','))
        new_s.append(i.split(','))

    print(new_s)
    new_s.sort(key = len)
    print(new_s)

    # for i in new_s:
    #     for j in range(len(i)):
    #         if int(i[j]) not in answer:
    #             answer.append(int(i[j]))

    return answer

# solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")