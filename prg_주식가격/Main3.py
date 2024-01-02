def solution(prices):
    stack = []
    answer = [0] * len(prices)

    for i in range(len(prices)):
        # print("------------------------")
        while stack != [] and stack[-1][1] > prices[i]:
            past, _ = stack.pop()
            answer[past] = i - past
            # print("answer : ",answer)

        stack.append([i, prices[i]])
        # print("stack : ", stack)

    # print("tmp_answer : ",answer)

    for i, s in stack:
        # print("-----")
        # print("answer : ",answer)
        answer[i] = len(prices) - 1 - i
    return answer

# solution([1, 2, 3, 2, 3])
# solution([3, 5, 1, 4, 6]) # [2, 1, 2, 1, 0]
solution([3, 5, 1, 4, 6, 10, 5]) # [2, 1, 4, 3, 2, 1, 0]
