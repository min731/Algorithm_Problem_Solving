def solution(n,a,b):
    answer = 0

    people = []

    for i in range(1,n+1):
        people.append(i)
    
    print(people)

    cnt = 0

    while True:
        cnt += 1

        if abs(people.index(a)-people.index(b)) == 1:
                if people.index(a) > people.index(b):
                     if people.index(a)%2==1:
                        print(a,b,cnt)
                        break
                else:
                     if people.index(b)%2==1:
                        print(a,b,cnt)
                        break

        print(a,b,cnt)

        length = len(people)

        for i in range(0,length,2):
            print("i",i,"people",people)
            if people[i+1] == a:
                people.append(people[i+1])
                continue
            elif people[i+1] == b:
                people.append(people[i+1])
                continue
            people.append(people[i])

        people = people[length:]

        print(people)

    answer = cnt

    return answer

answer = solution(8,4,7)
print("답 : " ,answer)
answer = solution(2,1,2)
print("답 : " ,answer)
answer = solution(4,2,3)
print("답 : " ,answer)
