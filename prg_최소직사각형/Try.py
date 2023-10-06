def solution(sizes):
    answer = 0

    start = sorted(sizes[0],reverse=True)
    big = start[0]
    small = start[1]

    for size in sizes:
        size = sorted(size,reverse=True)
        w, h = size

        print(size)
        print(w, h)
        
        if w>=big :
            big = w
        if h>=small:
            small = h

    answer = big*small
    print(answer)
    return answer

solution([[60, 50],[30, 70],[60, 30],[80, 40]])