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
    print(v_list)

    # print("-----------------------")
    while v_list:

        key,v = v_list.popleft()
        # print("v : ", v)

        k -= v
        answer += 1
        # print("answer : ",answer)
        # print("k : ",k)
        if k<=0:
            break
        
        # print("kinds : ",kinds)
        # print("key : ",key)
        del kinds[key]
        # answer += 1

    print(answer)
    return answer


solution(6,[1, 3, 2, 5, 4, 5, 2, 3])
solution(4,[1, 3, 2, 5, 4, 5, 2, 3])
solution(2,[1, 1, 1, 1, 2, 2, 2, 3])
solution(1,[1])
