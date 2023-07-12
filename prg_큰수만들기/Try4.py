def solution(number, k):
    import numpy as np
    cnt = len(number)-k
    answer = ''

    if cnt == 1:
        print(max(list(number)))
        return max(list(number))

    tmp = []
    # tmp = [1,9]
    tmp = number[:1-(cnt)]
    
    while cnt>0:

        print("-------------")
        # max_idx = 1
        print("tmp :",tmp)
        tmp = list(tmp)
        max_idx = np.argmax(tmp)
        print("max_idx : ",max_idx)
        # number = [2,4]
        number = number[max_idx+1:]
        print("number : ",number)
        # answer = 9
        answer += tmp[max_idx]
        print("answer : ",answer)

        cnt -= 1
        print("cnt : ",cnt)
        print("-(cnt-1) : ",-(cnt-1))
        if cnt == 1:
            answer += max(number)
            cnt -= 1

        tmp = number[:-(cnt-1)]

    print(answer)

    return answer

# solution("1924",2)
# solution("1231234",3)
# solution("4177252841",4)
# solution("121",1)
solution("11",1)

