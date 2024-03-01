def solution(sequence, k):
    answer = [len(sequence),0,len(sequence)-1]
    front = 0
    rear = 0
    tmp = sum(sequence[front:rear+1])
    len_seq = len(sequence)

    sequence += [0]
    print(sequence)
    print(answer) # [1,6,6]
    while front<=rear and front>=0 and rear<=len_seq-1:
        print("------------------------")
        print("front : ",front," rear : ",rear," tmp : ",tmp)

        if tmp==
            length = rear-front+1
            if length < answer[0]:
                print("길이 짧음!")
                answer = [length,front,rear]
            elif length == answer[0] and front<answer[1]:
                print("길이 같고, front 빠름!")
                answer = [length,front,rear]
            rear += 1
            tmp += sequence[rear]
        elif tmp<k:
            rear += 1
            tmp += sequence[rear]
        else:
            tmp -= sequence[front]
            front += 1
    
    print(answer[1:])
    return answer[1:]

# solution([1, 2, 3, 4, 5],7)
# solution([1, 1, 1, 2, 3, 4, 5],5)
solution([2, 2, 2, 2, 2],6)
