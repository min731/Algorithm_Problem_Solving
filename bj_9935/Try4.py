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


while origin_str1!=str1:

    tmp = ''
    while str1:

        for _ in range(n_bomb):
            tmp += str1.popleft()

        

print("ans:",str1)





# from collections import deque
# a = deque([1,2,3])
# b = deque([1,2,3])

# print(a==b)