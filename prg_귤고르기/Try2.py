def solution(k, tangerine):
    from collections import deque

    answer = 0
    kinds = {}
    for t in tangerine:
        try:
            kinds[t] += 1
        except:
            kinds[t] = 1
    
    v_list = deque(sorted(kinds.items(),key = lambda item: item[1]))
    print(v_list)

    while v_list:

        key,v = v_list.popleft()
        print("v : ", v)

        k -= v

        print("answer : ",answer)
        if k<=0:
            break
        
        print("kinds : ",kinds)
        # print("kinds.get(v) : ",kinds.get(v))
        del kinds[key]
        answer += 1
        
    print(answer)
    return answer


solution(6,[1, 3, 2, 5, 4, 5, 2, 3])
solution(4,[1, 3, 2, 5, 4, 5, 2, 3])
solution(2,[1, 1, 1, 1, 2, 2, 2, 3])