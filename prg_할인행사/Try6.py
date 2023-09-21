def solution(want, number, discount):
    from collections import deque,Counter
    
    answer = 0

    want_n = {w:n for w,n in zip(want,number)}
    # print(want_n)

    discount_queue = deque(discount)

    while len(discount_queue)>=10:
        
        is_answer = True
        print("------------------------")
        print("discount_queue : ",discount_queue)
        discount_counter = dict(Counter(list(discount_queue)[:10]))

        for k in discount_counter.keys():
            try :
                if discount_counter[k] == want_n[k]:
                    continue
                else:
                    is_answer = False
                    break
            except:
                is_answer = False
                break
        # print("want_n : ",want_n)
        # print("discount_counter : ",discount_counter)

        if is_answer:
            print("want_n : ",want_n)
            print("discount_counter : ",discount_counter)
            answer += 1
        discount_queue.popleft()

    print(answer)
    return answer

solution(["banana", "apple", "rice", "pork", "pot"],
         [3, 2, 2, 2, 1,],
         ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])
# solution(["apple"],
#          [10],
#          ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"])