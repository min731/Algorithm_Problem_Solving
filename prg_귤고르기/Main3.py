from collections import Counter

def solution(k, tangerine):
    result = 0
    answer = 0
    
    temp = Counter(tangerine)
    print(temp)
    temp = temp.most_common()
    print(temp)
    
    for i in temp:
        result += i[1]
        answer += 1
        if(result >= k):
            return answer
        
solution(6,[1, 3, 2, 5, 4, 5, 2, 3])
# solution(4,[1, 3, 2, 5, 4, 5, 2, 3])
# solution(2,[1, 1, 1, 1, 2, 2, 2, 3])
# solution(1,[1])