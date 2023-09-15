def solution(k, tangerine):
    from collections import deque

    answer = 0
    kinds = {}
    for t in tangerine:
        try:
            kinds[t] += 1
        except:
            kinds[t] = 1
    
    v_list = deque(sorted(kinds.items(),key = lambda item: item[1],reverse=True))

    # print("-----------------------")
    while v_list:

        key,v = v_list.popleft()

        k -= v
        answer += 1

        if k<=0:
            break
        
        del kinds[key]

    return answer