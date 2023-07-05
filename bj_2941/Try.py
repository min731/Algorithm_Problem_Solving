word = str(input())

from collections import deque

word =deque(word)
cro = {'c=':0,'c-':0,'dz=':0,'d-':0,'lj':0,'nj':0,'s=':0,'z=':0}
check = set()
cnt = 0

while word:
    
    print("word : ",word)
    print("-----")
    # e
    el1 = word.popleft()
    print("el1 : ",el1)
    try:
        # s 
        el2 = word.popleft()
        print("el2 : ",el2)
        if el1+el2 in cro.keys():
            # print("cro!")
            print("add : ",el1+el2)
            check.add(el1+el2)
            continue
            # cnt += 1
        else:
            # print("el2 넣음 : ",el2)
            word.appendleft(el2)
            # print("no cro!")
            print("add : ",el1)
            check.add(el1)
            continue
            # cnt += 1
    except:
        pass
    
    # print("no cro!")
    # print(el1)
    check.add(el1)

print(len(check))