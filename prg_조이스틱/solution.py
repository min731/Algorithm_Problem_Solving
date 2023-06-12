def solution(name):
    answer = 0
    # A : 65
    # Z : 90


    done = [2 if x == 'A' else False for x in name]
    idx = 0
    done[idx] = True

    while True:

        if 77 - ord(name[idx]) >=0:
            # print((ord(str1) - 65))
            answer += (ord(name[idx]) - 65)    
        else:
            # print((91 - ord(str1)))
            answer += (91 - ord(name[idx]))

        done[idx] = True

        print("done :", done)
        print("name[idx] : ",name[idx])
        print("answer : ",answer)

        if False not in done:
            break

        add_idx = 0

        while True:

            add_idx += 1

            print("idx+add_idx", idx+add_idx,"idx-add_idx",idx-add_idx)
            if done[idx+add_idx] == True or done[idx+add_idx] !=2:
                idx = idx+add_idx
                done[idx] = True
            
            if done[idx-add_idx] != True or done[idx-add_idx] !=2:
                idx = idx-add_idx
                done[idx] = True
            
            if done[idx] :
                answer += add_idx
                break

    return answer

solution("JEROEN")