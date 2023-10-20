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

    return answer