def solution(sequence, k):
    answer = []
    front = 0
    rear = 1
    tmp = 0
    
    while front>=0 and front<rear:
        print("------------------------")
        tmp = sum(sequence[front:rear+1])
        print("front : ",front," rear : ",rear," tmp : ",tmp)

        if tmp==k:
            answer.append([rear-front+1,front,rear])
            rear -= 1
        elif tmp<k:
            rear += 1
        else:
            front += 1
    
    print(answer)
    
    return answer

# solution([1, 2, 3, 4, 5],7)
solution([1, 1, 1, 2, 3, 4, 5],5)
# solution([2, 2, 2, 2, 2],6)
