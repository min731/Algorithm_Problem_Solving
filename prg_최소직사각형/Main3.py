def solution(sizes):
    
    allWidth = []
    allHeight = []
    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]
        
        allWidth.append(size[0])
        allHeight.append(size[1])

    return max(allWidth) * max(allHeight)