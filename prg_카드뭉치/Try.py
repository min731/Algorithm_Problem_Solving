def solution(cards1, cards2, goal):
    answer = ''

    cnt = len(goal)

    while cnt > 0 :

        target = goal.pop()

        print(target)

        if len(cards1) != 0 and cards1[-1] == target:
            cards1.pop()
        elif len(cards2) != 0 and cards2[-1]== target:
            cards2.pop()
        else:
            answer = "No"
            print(answer)
            return answer
        cnt -= 1

    answer = "Yes"

    print(answer)
    return answer

# solution(["i", "drink", "water"], ["want", "to"],["i", "want", "to", "drink", "water"])
# solution(["i", "drink", "water"], ["want", "to","hot"],["i", "want", "to", "drink","hot","water"])
# solution([], ["i", "want", "to", "drink","hot","water"],["i", "want", "to", "drink","hot","water"])
# solution([], [],["i", "want", "to", "drink","hot","water"])
# solution([], [],[])
# solution(["i", "drink", "water"], ["want", "to"],["i", "want", "to", "drink", "water"])
solution(["i", "drink", "water"], ["want", "to", "juice"], ["i", "want", "to", "drink", "water"])