def lower_bound(cards,target):

    start, end = 0,len(cards)

    while start<end:
        mid = (start+end)//2

        if cards[mid]<=target:
            start = mid
        elif cards[mid]>target:
            end = mid-1
    
    return start

def upper_bound(cards,target):

    start, end = 0,len(cards)

    while start<end:
        mid = (start+end)//2

        if cards[mid]<target:
            start = mid+1
        elif cards[mid]>target:
            end = mid-1
    
    return start


            

N = int(input())
cards = list(map(int,input().split()))
cards.sort()
print(cards)

M = int(input())
check = list(map(int,input().split()))