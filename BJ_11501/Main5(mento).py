t= int(input())
from collections import Counter
for _ in range(t):
    k = int(input())
    tmpList = input().split()

    # 10 7 6
    tmpList = list(map(int, tmpList))
    dic = dict(Counter(tmpList))
    # sortedDic = {10:1,7:1,6:1}
    sortedDic = dict(sorted(dic.items(), key=lambda x: x[0]))
    keysList = list(sortedDic.keys())
    print(keysList)

    # 제일 비싼 주식
    maxN = keysList[-1]
    answer = 0
    
    # 구매 목록
    tmp = []
    
    # 5 9 7 9
    for i in tmpList:
        if i == maxN:
            sortedDic[maxN] -= 1
            if sortedDic[maxN] == 0:
                answer += sum(maxN - k for k in tmp)
                keysList.pop()
                maxN = keysList[-1]
                tmp = []

            if len(keysList) == 1:
                break
        else:
            sortedDic[i] -= 1
            if sortedDic[i] == 0:
                keysList.remove(i)
            tmp.append(i)
    print(answer)