N = int(input())
ans = 0
find = False

if N%5==0:
    ans = N//5
    find = True
else:
    bongji5 = N//5+1 # 5kg 봉지 갯수
    # bongji3 = 0 # 3kg 봉지 갯수

    while bongji5>=0:

        rest = N-bongji5*5

        if rest<0:
            bongji5 -= 1
        elif rest>0:
            if rest%3==0:
                ans = bongji5+rest//3
                find = True
                break
            else:
                bongji5 -= 1

if find:
    print(ans)
else:
    print(-1)