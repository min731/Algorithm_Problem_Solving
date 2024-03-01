def solution(sequence, k):
    answer = []
    front = 0
    rear = 1
    tmp = 0

    if k in sequence:
        answer.append([1,sequence.index(k),sequence.index(k)])
    
    while front<rear and front>=0 and rear <= len(sequence)-1:
        print("------------------------")
        tmp = sum(sequence[front:rear+1])
        print("front : ",front," rear : ",rear," tmp : ",tmp)

        if tmp==k and [rear-front+1,front,rear] not in answer:
            answer.append([rear-front+1,front,rear])
            rear -= 1
        elif tmp<k:
            rear += 1
        else:
            front += 1
    
    print(answer)
    answer.sort()
    print(answer[0][1:])
    return answer[0][1:]

# solution([1, 2, 3, 4, 5],7)
solution([1, 1, 1, 2, 3, 4, 5],5)
# solution([2, 2, 2, 2, 2],6)
