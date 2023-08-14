def solution(data, col, row_begin, row_end):
    answer = 0
    hash = {}

    idxes = []
    col_v = []
    for idx,data1 in enumerate(data):
        hash[idx] = data1
        idxes.append(idx)
        col_v.append(hash[idx][col-1])

    print(col_v)

    col_v.sort()

    hash_sort = {}
    # for k,y in hash.items():
        

    # for idx in idxes:
    #     if 



    # print(hash)    
    return answer

solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]],2,2,3)