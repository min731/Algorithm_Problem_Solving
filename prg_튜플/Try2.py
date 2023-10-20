import re
from collections import Counter

def solution(s):
    answer = []
    
    s = re.findall('\d+', s)
    # print(s)
    s = Counter(s)
    # print(s.items())

    s = sorted(s.items(),key= lambda x:x[1],reverse=True)

    for x in s:
        answer.append(int(x[0]))

    print(answer)
    return answer

solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")



# t1 = '[[20,111],[20]]'
# print(type(eval(t1)))