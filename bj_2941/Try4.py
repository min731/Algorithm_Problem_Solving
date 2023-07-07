word = list(input())
from collections import deque
word = deque(word)

cro = {'c=':2,'c-':2,'dz=':3,'d-':2,'lj':2,'nj':2,'s=':2,'z=':2}
cnt = 0

while word:

    print("------")
    el1 = word.popleft()
    try:
        el2 = word.popleft()
        if el1+el2 in cro.keys():
            cnt += 1
            print(word)
            print(cnt)
            continue
        else:
            word.appendleft(el2)
        try: 
            el2 = word.popleft()
            el3 = word.popleft()
            if el1+el2+el3 in cro.keys():
                cnt += 1
                print(word)
                print(cnt)
                continue
            else:
                word.appendleft(el3)
                word.appendleft(el2)
        except:
            word.appendleft(el2)
    except:
        pass
    cnt += 1

    print(word)
    print(cnt)


print(cnt)