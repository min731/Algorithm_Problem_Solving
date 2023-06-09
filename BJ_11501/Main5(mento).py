import sys
input = sys.stdin.readline

t= int(input())
from collections import Counter
for _ in range(t):
    k = int(input())
    tmpList = input().split()
    tmpList = list(map(int, tmpList))
    dic = dict(Counter(tmpList))
    sortedDic = dict(sorted(dic.items(), key=lambda x: x[0]))
    keysList = list(sortedDic.keys())
    maxN = keysList[-1]
    answer = 0
    tmp = []
    for i in tmpList:
        if i == maxN:
            sortedDic[maxN] -= 1
            if sortedDic[maxN] == 0:
                answer += sum(maxN - k for k in tmp)
                keysList.pop()
                try:
                    maxN = keysList[-1]
                except:
                    break
                tmp = []
            if len(keysList) == 1:
                break
        else:
            sortedDic[i] -= 1
            if sortedDic[i] == 0:
                keysList.remove(i)
            tmp.append(i)
    print(answer)