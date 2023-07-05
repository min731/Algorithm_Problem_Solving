word = str(input())

from collections import deque

# word =deque(word)
cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt = 0

for i in range(len(cro)):

    print("-----")
    print("전 : ",word)
    print(cro[i])
    before = len(word)
    word = word.replace(cro[i],"")
    print("후 : ",word)
    after = len(word)

    if before != after:
        cnt += 1

cnt += len(word)

print(cnt)