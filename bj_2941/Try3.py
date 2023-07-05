word = str(input())

from collections import deque

word =deque(word)
cro = cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
check = set()
cnt = 0

while word:
    
    try:
        el1 = word.popleft()
        el2 = word.popleft()
        el3 = word.popleft()

        if el1+el2+el3 in cro:
            cnt += 1
        else:
            word.popleft(el3)
    
    except:
        

print(len(check))