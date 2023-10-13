def solution(s, n):

    answer = ''

    uppers = [chr(i) for i in range(65,91)]
    lowers  = [chr(i) for i in range(97,123)]

    for x in s:

        if x==" ":
            answer += " "
            continue

        if x.islower(): # 소문자
  
            answer += lowers[(lowers.index(x)+n%26)%26]
        else: # 대문자

            answer += uppers[(uppers.index(x)+n%26)%26]
            
    return answer

solution("AB",1)
solution("z",1)
solution("a B z",4)
solution("ZzZz",33)