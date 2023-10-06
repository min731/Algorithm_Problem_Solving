def solution(sizes):
    answer = 0

    start = sorted(sizes[0],reverse=True)
    big = start[0]
    small = start[1]

    for size in sizes:
        size = sorted(size,reverse=True)
        w, h = size

        
        if w>=big :
            big = w
        if h>=small:
            small = h

    answer = big*small

    return answer