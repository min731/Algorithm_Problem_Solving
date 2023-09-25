def solution(citations):
    answer = 0
    citations.sort()

    for i in range(0,citations[-1]+1):
        over = 0
        under = 0
        for c in citations:
            if c==i:
                over += 1
                under += 1
            if c>i:
                over += 1
            elif c<i:
                under += 1
        if over>=i and i>=under:
            if i>answer:
                answer = i
    return answer

solution([3, 0, 6, 1, 5])