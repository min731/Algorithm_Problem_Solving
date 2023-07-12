def solution(number, k):
    import numpy as np
    length = len(number)-k
    answer = ''

    tmp = []
    # tmp = [1,9]
    tmp = number[:k]

    while len(answer) != length:
        print("-------------")
        print("tmp : ",tmp)
        # max_idx = 1
        tmp = list(tmp)
        max_idx = np.argmax(tmp)
        print("max_idx : ",max_idx)
        # number = [2,4]
        number = number[max_idx+1:]
        print("number : ",number)
        # answer = 9
        answer += tmp[max_idx]
        print("answer : ",answer)

        tmp = number[:-(length-len(answer))]
        print("tmp :",tmp)

    print(answer)

    return answer

# solution("1924",2)
solution("1231234",3)
# solution("4177252841",4)
