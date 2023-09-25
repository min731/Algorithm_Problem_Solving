def solution(citations):
    citations = sorted(citations)
    print(citations)
    l = len(citations)
    for i in range(l):
        print("citations[i] : ",citations[i]," l-i : ",l-i)
        if citations[i] >= l-i:
            return l-i
    return 0



solution([3, 0, 6, 1, 5])