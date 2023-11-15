def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        print(a12)
        a12=a12.rjust(n,'0')
        print(a12)
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
