def solution(s):
    answer = 0
    stack = s.split()

    print(stack)

    while stack:

        v = stack.pop()

        if v == "Z":

            v = stack.pop()
            continue

        answer += int(v)

    print(answer)
    return answer


solution("-1 -2 -3 Z")