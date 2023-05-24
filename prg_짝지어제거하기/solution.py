def solution(s):

    answer = -1

    stack = []

    for el in s:
        if len(stack) == 0 :
            stack.append(el)
        elif stack[-1] == el:
            stack.pop()
        else:
            stack.append(el)

    if len(stack) == 0:
        answer = 1
    else :
        answer = 0

    return answer