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
            
            tmp = deque([])
            while people:
                p2 = people.pop()
                print("p2 : ",p2)

                if p1+p2<=limit:
                    break
                else:
                    tmp.appendleft(p2)
            people += tmp

            print("people : ",people)

        except:
            pass

        answer += 1
    
    print(answer)
    return answer


# solution([70, 50, 80, 50],100)
# solution([70, 80, 50],100)

# solution([50],100)
solution([50,70,100,150,190,200],200)
# solution([10,20,80,90],100)
# solution([20,50,80,90],100)


# from collections import deque

# list1 = deque(['str1','str2'])

# list1.popleft()
# print(list1)