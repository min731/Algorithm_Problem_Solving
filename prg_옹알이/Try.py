def solution(babbling):
    answer = 0

    while babbling:

        prns = ["aya", "ye", "woo", "ma" ]

        word = babbling.pop()
        print("단어 : ", word) 

        while True:
                
            len1 = len(word)

            for prn in prns:
                
                find = word.find(prn)

                if find == 0:
                    word = word[len(prn):]
                    prns.remove(prn)

                r_find = word.rfind(prn)

                if r_find == len(word)-1-len(prn):
                    word = word[:len(prn)]
                    prns.remove(prn)
                print("제거된 word :", word)

            len2 = len(word)
            
            if len1 == len2:
                break

        if word == "":
            print("제거 : ",word)
            answer += 1

    print(answer)

    return answer

solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"])
# solution(["mayewooyeye"])


# word = "abcd"

# r_find = word.rfind("ab")

# print(r_find)