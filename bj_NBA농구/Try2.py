N = int(input())
score1, lead1 = 0,0
score2, lead2 = 0,0
now = 0

for _ in range(N):
    print("--------")
    team, time = map(str,input().split())
    print(team,time)
    minutes, seconds = list(map(int,time.split(":")))
    time = minutes*60+seconds
    print("time : ",time)
    
    if score1>score2:
        lead1 += time-now
    elif score1<score2:    
        lead2 += time-now

    now = time

    if team=='1':
        # print("1팀 득점")
        score1 += 1
    else:
        # print("2팀 득점")
        score2 += 1
    print("score1 : ",score1, "score2 : ",score2)

if score1>score2:
    lead1 += 48*60-now
elif score1<score2:    
    lead2 += 48*60-now

print("--ans--")
print(f'{lead1//60:02d}:{lead1%60:02d}')
print(f'{lead2//60:02d}:{lead2%60:02d}')
# print(str(lead1//60)+':',lead1%60)
# print(str(lead2//60)+':',lead2%60)