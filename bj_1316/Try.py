N = int(input())

words = []
for _ in range(N):
    words.append(str(input()))

cnt = 0

for word in words:
    check = [chr(x) for x in range(97,123)]
    check.remove(word[0])
    rep = False
    print("------------------------------")
    for i in range(1,len(word)):
        if word[i-1] == word[i]:
            continue
        try:
            check.remove(word[i])
        except:
            rep = True
            break
        print("word[i] : ",word[i])
        print("check : ",check)
                
    if not rep:
        cnt += 1

print(cnt)