str1 = input()
bomb = input()

# print(str1)
# print(bomb)

from collections import deque
str1 = deque(str1)
print(str1)
n_bomb = len(bomb)

origin_str1 = deque(str1.copy())

cnt = 0
while origin_str1!=str1.rotate(1):
    cnt += 1
    print("--------------------------")
    print(origin_str1)
    print(str1)
    print(origin_str1==str1)
    print("--------------------------")
    
    if cnt == 20:
        break

# while bomb in str1:
#     str1 = str1.replace(bomb,"")

# if str1=="":
#     print("FRULA")
# else:
#     print(str1)





# from collections import deque
# a = deque([1,2,3])
# b = deque([1,2,3])

# print(a==b)