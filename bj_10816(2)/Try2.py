def lower_bound(cards,target):

    start, end = 0,len(cards)

    while start<end:
        mid = (start+end)//2

        if cards[mid]<target:
            start = mid+1
        else:
            end = mid

    print("lower : ",start)
    return start

def upper_bound(cards,target):

    start, end = 0,len(cards)

    while start<end:
        mid = (start+end)//2

        # 값 찾아도 +1올림
        if cards[mid]<=target:
            start = mid+1
        else:
            end = mid
    print("upper : ",start-1)
    return start-1


            

N = int(input())
cards = list(map(int,input().split()))
cards.sort()
print(cards)

M = int(input())
check = list(map(int,input().split()))

for x in check:
    print("------")
    lower = lower_bound(cards,x)
    upper = upper_bound(cards,x)
    print(upper-lower+1)