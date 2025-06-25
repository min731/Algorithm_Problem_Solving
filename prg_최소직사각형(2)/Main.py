def solution(sizes):
    
    max_num = max(sum(sizes,[]))
    print(max_num)
    
    other = 0
    
    for x, y in sizes:
        if x > y and y > other:
            other = y
        elif x <= y and x > other:
            other = x
               
    return max_num*other


if __name__ == "__main__":
    print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
    print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
    print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))