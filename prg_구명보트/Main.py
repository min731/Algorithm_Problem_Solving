from bisect import bisect_right
from collections import deque

def solution(people, limit):
    people.sort()
    time =0
    people = deque(people)
    while people:

        print("------------")
        print("people :",people)

        first = people.pop()
        left = limit-first
        print("left : ",left)
        if people and left>=people[0]:
            
            if piv := bisect_right(people,left):
                print("piv : ",piv)
                del people[piv-1]
        time +=1
    return time


# solution([70, 50, 80, 50],100)
# solution([70, 80, 50],100)

# solution([50],100)
# solution([50,70,100,150,190,200],200)
solution([50,70,100,150,190],200)
# solution([10,20,80,90],100)
# solution([20,50,80,90],100)
