def solution(arr1, arr2):
    answer = []

    transposed_arr2 = []

    for col in range(len(arr2[0])):
        new_row = []
        for row in range(len(arr2)):
            new_row.append(arr2[row][col])
        transposed_arr2.append(new_row)

    for v1 in arr1:
        
        tmp = []
        for v2 in transposed_arr2:
            tmp.append(sum([x*y for x,y in zip(v1,v2)]))
        
        answer.append(tmp)

    return answer

# solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]])
solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],[[5, 4, 3], [2, 4, 1], [3, 1, 1]])
