def solution(babbling):
    answer = 0

    prns = ["aya", "ye", "woo", "ma" ]

    while babbling:

        word = babbling.pop()
        print("단어 : ", word)
        print(prns)

        while True:
                
            len1 = len(word)

            for prn in prns:
                
                find = word.find(prn)

                print("현재 prn : ",prn)
                
                if find == 0:
                    word = word[len(prn):]

                if find == len(word)-1-len(prn):
                    word = word[:len(prn)+1]

            len2 = len(word)
            
            if len1 == len2:
                break

        if word == "":
            print("제거 : ",word)
            answer += 1

    print(answer)

    return answer

solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"])

