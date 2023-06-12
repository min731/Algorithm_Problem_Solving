def solution(name):
    answer = 0

    # 최소 이동 횟수
    min_move = len(name)-1

    for idx,str1 in enumerate(name):
        
        print("idx", idx, "str1",str1)

        if 77 - ord(str1) >=0:
            print((ord(str1) - 65))
            answer += (ord(str1) - 65)    
        else:
            print((91 - ord(str1)))
            answer += (91 - ord(str1))

        next = idx+1

        while next < len(name) and name[next] == 'A':
            next += 1

        print([min_move,idx+idx+len(name)-next,idx+2*(len(name)-next)])        
        min_move = min([min_move,idx+idx+len(name)-next,idx+2*(len(name)-next)])


    answer += min_move

    print(answer)
    return answer

solution("JEROEN")