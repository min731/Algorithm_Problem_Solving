def solution(want, number, discount):
    from collections import deque,Counter
    
    answer = 0

    # want_n = {w:n for w,n in zip(want,number)}
    # print(want_n)

    want_n = {}
    for i in range(len(want)):
        want_n[want[i]] = number[i]
        
    discount_queue = deque(discount)

    while len(discount_queue)>=10:
        print("------------------------")
        print("discount_queue : ",discount_queue)
        discount_counter = dict(Counter(list(discount_queue)[:10]))

        if discount_counter == want_n:
            answer += 1

        print("want_n : ",want_n)
        print("discount_counter : ",discount_counter)

        discount_queue.popleft()

    print(answer)
    return answer

# solution(["banana", "apple", "rice", "pork", "pot"],
#          [3, 2, 2, 2, 1,],
#          ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])
solution(["apple"],
         [10],
         ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"])