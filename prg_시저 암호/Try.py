def solution(s, n):
    print("----------------------")
    answer = ''
    print(s)
    for x in s:
        
        if x==" ":
            print(x, " 는 공백")
            answer+=x
            continue

        if x.islower(): # 소문자
            print(x, " 는 소문자")
            answer += chr(96+(ord(x)+n)%96)
        else: # 대문자
            print(x, " 는 대문자")
            answer += chr(64+ (ord(x)+n)%64)

    print(answer)
    # print(66%65)  
    return answer

solution("AB",1)
solution("z",1)
solution("a B z",4)