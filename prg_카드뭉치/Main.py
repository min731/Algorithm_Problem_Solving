def solution(cards1, cards2, goal):
    from collections import deque

    answer = ''

    goal = deque(goal)

    while goal :

        target = goal.popleft()

        if len(cards1) != 0 and cards1[0] == target:
            cards1 = cards1[1:]
        elif len(cards2) != 0 and cards2[0]== target:
            cards2 = cards2[1:]
        else:
            answer = "No"
            print(answer)
            return answer
        
    answer = "Yes"

    print(answer)
    return answer

solution(["i", "drink", "water"], ["want", "to"],["i", "want", "to", "drink", "water"])
solution(["i", "drink", "water"], ["want", "to","hot"],["i", "want", "to", "drink","hot","water"])
solution([], ["i", "want", "to", "drink","hot","water"],["i", "want", "to", "drink","hot","water"])
solution([], [],["i", "want", "to", "drink","hot","water"])
solution([], [],[])
solution(["i", "drink", "water"], ["want", "to"],["i", "want", "to", "drink", "water"])