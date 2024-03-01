def solution(sequence, k):
    answer = [len(sequence),0,len(sequence)-1]
    front = 0
    rear = 1
    tmp = sequence[:2]
    if k in sequence:
        answer = [1,sequence.index(k),sequence.index(k)]

    print(answer) # [1,6,6]
    while front<rear and front>=0 and rear<=len(sequence)-1:
        print("------------------------")
        tmp = sum(sequence[front:rear+1])
        print("front : ",front," rear : ",rear," tmp : ",tmp)

        if tmp==k:
            length = rear-front+1
            if length < answer[0]:
                print("길이 짧음!")
                answer = [length,front,rear]
            elif length == answer[0] and front <answer[1]:
                print("길이 같고, front 빠름!")
                answer = [length,front,rear]
            rear += 1
        elif tmp<k:
            rear += 1
        else:
            front += 1
    
    print(answer[1:])
    return answer[1:]

# solution([1, 2, 3, 4, 5],7)
solution([1, 1, 1, 2, 3, 4, 5],5)
# solution([2, 2, 2, 2, 2],6)
