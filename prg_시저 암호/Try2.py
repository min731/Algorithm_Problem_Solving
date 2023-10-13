def solution(s, n):

    print("---------------------------------")
    answer = ''

    uppers = [chr(i) for i in range(65,91)]
    lowers  = [chr(i) for i in range(97,123)]
    print("uppers : ",uppers)
    print("lowers : ",lowers)
    for x in s:

        if x==" ":
            answer += " "
            continue

        if x.islower(): # 소문자
            print(x, "는 소문자" )
            print("인덱스 : ",lowers.index(x))
            print("추가 인덱스 : ",n%26)
            answer += lowers[(lowers.index(x)+n%26)%26]
        else: # 대문자
            print(x, "는 대문자" )
            print("인덱스 : ",uppers.index(x))
            print("추가 인덱스 : ",n%26)
            answer += uppers[(uppers.index(x)+n%26)%26]

    print(answer)
    return answer

solution("AB",1)
solution("z",1)
solution("a B z",4)
solution("ZzZz",33)