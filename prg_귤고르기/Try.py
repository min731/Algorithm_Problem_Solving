def solution(k, tangerine):
    from collections import deque

    answer = 0
    kinds = {}
    for t in tangerine:
        try:
            kinds[t] += 1
        except:
            kinds[t] = 1
    
    v_list = deque(sorted(kinds.values(),reverse=True))
    print(v_list)

    while v_list:

        v = v_list.popleft()
        print("v : ", v)

        answer += v

        print("answer : ",answer)
        if answer>=k:
            break
        
        print("kinds : ",kinds)
        print("kinds.get(v) : ",kinds.get(v))
        kinds.pop(kinds.get(v))
        

    return answer


solution(6,[1, 3, 2, 5, 4, 5, 2, 3])