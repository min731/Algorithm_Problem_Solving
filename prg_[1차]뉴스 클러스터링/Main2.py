import re
import math

def solution(str1, str2):

    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    print(str1)
    print(str2)

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    print(gyo)
    print(hap)
    if len(hap) == 0:
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo]) # 교
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap]) # 합

    return math.floor((gyo_sum/hap_sum)*65536)

solution('FRANCE','french')
# solution('aa1+aa2','AAAA12')