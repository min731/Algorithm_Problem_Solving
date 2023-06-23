def solution(babbling):
    answer = 0

    prns = ["aya", "ye", "woo", "ma" ]

    while babbling:

        word = babbling.pop()

        while True:
                
            len1 = len(word)

            for prn in prns:
                
                find = word.find(prn)
                
                if find == 0:
                    word = word[len(prn):]

                if find == len(word)-1-len(prn):
                    word = word[:len(prn)+1]

            len2 = len(word)
            
            if len1 == len2:
                break

        if word == "":
            answer += 1

    return answer

solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"])

