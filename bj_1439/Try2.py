S = list(str(input()))

last = S[0]
S.append(last)

cnt = 0
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        cnt += 1

print(int(cnt/2))