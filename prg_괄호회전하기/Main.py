def solution(s):

    answer = 0

    from collections import deque

    s = deque(s)
    length = len(s)

    cnt = 0
    while cnt!=length:
        
        s_tmp = s.copy()
        save = ''

        while s_tmp:

            v = s_tmp.popleft()
            save += v

            try :

                if save[-2:] in ['[]','{}','()']:
                    save = save.replace(save[-2:],'')
            except:
                pass

        if save=='':
            answer += 1

        s.rotate(1)
        cnt += 1

    return answer

solution("[](){}")
solution("}]()[{")