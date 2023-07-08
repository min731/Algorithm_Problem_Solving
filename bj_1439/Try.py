S = list(str(input()))

idx = 0
length = len(S)
before = S[idx]

while idx < length:
    now = S[idx+1]

    if before != now:
        