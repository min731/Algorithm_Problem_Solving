def solution(s):
    answer = []
    
    s = s.replace("{","[")
    s = s.replace("}","]")
    s = eval(s)
    s.sort(key=lambda x : len(x))

    print(s)

    answer.append(s[0][0])

    for el in s:
        for x in el:
            if x not in answer:
                answer.append(x)

    print(answer)
    return answer

# solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")



# t1 = '[[20,111],[20]]'
# print(type(eval(t1)))