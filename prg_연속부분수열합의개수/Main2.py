def solution(elements):
    answer = 0
    cycle = elements + elements
    s = []
    for i in range(len(elements)):
        for j in range(len(elements)):
            print(" i : i+j :",i , i+j)
            print(cycle[i:i+j])
            s.append(sum(cycle[i:i+j]))

    print(set(s))
    return len(set(s))

solution([1,2,3])