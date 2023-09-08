def solution(people, limit):

    answer = 0

    people.sort()
    n_people = len(people)

    people1 = people[:int(n_people/2)]
    people2 = people[int(n_people/2):]

    print("people : ",people1)
    print("people : ",people2)

    while people1 or people2:
        
        p1 = people1.pop()
         

    return answer


# solution([70, 50, 80, 50],100)
# solution([70, 80, 50],100)

# solution([50],100)
# solution([50,70,100,150,190,200],200)
solution([50,70,100,150,190],200)
# solution([10,20,80,90],100)
# solution([20,50,80,90],100)


# from collections import deque

# list1 = deque(['str1','str2'])

# list1.popleft()
# print(list1)



# from bisect import bisect_left, bisect_right

# nums = [4, 5, 5, 5, 5, 5, 5, 5, 5, 6]
# n = 5

# print(bisect_left(nums, n))
# print(bisect_right(nums, n))