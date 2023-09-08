def solution(people, limit):

    answer = 0

    from collections import deque

    people.sort()

    people = deque(people)

    print("people : ",people)

    while people:
        
        print("---------------------")
        p1 = people.popleft()
        
        print("p1 : ",p1)
        try:
            p2 = people.popleft()
            print("p1 : ",p2)

            if p1+p2<=limit:
                pass
            else:
                people.appendleft(p2)
        except:
            pass

        answer += 1
    
    print(answer)
    return answer


# solution([70, 50, 80, 50],100)
# solution([70, 80, 50],100)

solution([50],100)
solution([50,70,100,150,200,240],200)


# from collections import deque

# list1 = deque(['str1','str2'])

# list1.popleft()
# print(list1)