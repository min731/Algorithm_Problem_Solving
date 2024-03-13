def solution(babbling):
    answer = 0
    
    checkes = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        # print("---------------")
        # print(word)
        before = ''
        canFind = True
        
        while canFind:            
            canFind = False

            for check in checkes:
                if word.startswith(check):
                    if check==before:
                        canFind = False                    
                        break
                    word = word[len(check):]
                    # print(word)
                    canFind = True
                    before = check
                    break
                    
        if word=='':
            answer += 1
    
    return answer