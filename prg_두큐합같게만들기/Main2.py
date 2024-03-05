def solution(queue1, queue2):
    _sum = (sum(queue1) + sum(queue2)) // 2
    
    if (max(queue1 + queue2) > _sum) : return -1
    
    answer, start1, start2 = 0, 0, 0
    end1, end2 = len(queue1) - 1, len(queue1) - 1
    lst1 = queue1 + queue2 + queue1
    lst2 = queue2 + queue1 + queue2
    sum1, sum2 = sum(queue1), sum(queue2)
    
    while sum1 != _sum and sum2 != _sum :

        print("-----------------------------")
        print("queue1 : ",lst1[start1:end1+1], " sum1 :",sum(lst1[start1:end1+1]))
        print("queue2 : ",lst2[start2:end2+1], " sum2 :",sum(lst2[start2:end2+1]))

        
        if sum1 < _sum :
            end1 += 1
            if end1 == len(lst1) : return -1
            sum1 += lst1[end1]
        else :
            sum1 -= lst1[start1]
            start1 += 1
        
        if sum2 < _sum :
            end2 += 1
            if end2 == len(lst2) : return -1
            sum2 += lst2[end2]
        else :
            sum2 -= lst2[start2]
            start2 += 1
        answer += 1
    return answer

# solution([3, 2, 7, 2],[4, 6, 5, 1])
solution([1, 2, 1, 2],[1, 10, 1, 2])