def solution(s):
    answer = False
    
    n = len(s)

    if n==4 or n==6:
        if s.isnumeric():
            answer = True

    print(answer)
    return answer

solution("a234")
solution("1234"	)