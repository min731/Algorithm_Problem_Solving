def solution(s):

    answer = 0

    from collections import deque

    s = deque(s)
    length = len(s)

    cnt = 0
    while cnt!=length:
        
        s_tmp = s.copy()
        save = ''
        is_correct = True
        print("------------------------")
        while s_tmp:
            print("s_tmp : ",s_tmp)
            print("save : ",save)
            v = s_tmp.popleft()
            save += v

            try :
                print("save[-2:] : ",save[-2:])
                if save[-2:] in ['[]','{}','()']:
                    save = save.replace(save[-2:],'')
            except:
                pass

        if save=='':
            answer += 1

        s.rotate(1)
        cnt += 1

    print(answer)
    return answer

solution("[](){}")
solution("}]()[{")