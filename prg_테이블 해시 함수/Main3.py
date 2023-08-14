from functools import reduce
def solution(data, col, row_begin, row_end):

    data.sort(key=lambda x:(x[col-1],-x[0]))
    print([sum(map(lambda x: x%(i+1),data[i])) for i in range(row_begin-1, row_end)])
    answer = reduce(lambda x,y:x^y,[sum(map(lambda x: x%(i+1),data[i])) for i in range(row_begin-1, row_end)])
    return answer

solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]],2,2,3)


numbers = [2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print("Product:", product)