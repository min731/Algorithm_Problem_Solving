N = int(input())
score1, lead1 = 0,0
score2, lead2 = 0,0
now = 0

for _ in range(N):
    team, time = map(str,input().split())
    minutes, seconds = list(map(int,time.split(":")))
    time = minutes*60+seconds
    
    if score1>score2:
        lead1 += time-now
    elif score1<score2:    
        lead2 += time-now

    now = time

    if team=='1':
        score1 += 1
    else:
        score2 += 1

if score1>score2:
    lead1 += 48*60-now
elif score1<score2:    
    lead2 += 48*60-now

print(f'{lead1//60:02d}:{lead1%60:02d}')
print(f'{lead2//60:02d}:{lead2%60:02d}')
