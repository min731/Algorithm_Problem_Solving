str1 = input()
bomb = input()

# print(str1)
# print(bomb)

while bomb in str1:
    str1 = str1.replace(bomb,"")

if str1=="":
    print("FRULA")
else:
    print(str1)