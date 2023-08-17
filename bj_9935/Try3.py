str1 = input()
bomb = input()

# print(str1)
# print(bomb)

from collections import deque
import itertools
str1 = deque(str1)
print(str1)
n_bomb = len(bomb)

origin_str1 = deque(str1.copy())
str1.rotate(1)

while origin_str1!=str1:
    if ''.join(list(itertools.islice(str1, 0,n_bomb)))==bomb:
        # str1 = deque(str1)
        for _ in range(n_bomb):
            str1.popleft()
        origin_str1 = deque(str1.copy())
        # continue
    str1.rotate(1)
    print(origin_str1)
    print(str1)

if str1=="":
    print("FRULA")
else:
    print(str1)
print("ans:",str1)





# from collections import deque
# a = deque([1,2,3])
# b = deque([1,2,3])

# print(a==b)