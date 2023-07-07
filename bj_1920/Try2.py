
def bs(array,check):
    from bisect import bisect

    # N = int(input())
    # array = list(map(int,input().split()))
    # array = sorted(array)

    max_idx = len(array)-1

    # M = int(input())
    # check = list(map(int,input().split()))

    for x in check:
        v = bisect(array,x)
        print("x : ",x)
        print("v-1 : ",v-1)
        print("array[v-1] : ",array[v-1])

        if v-1 == 0 or v-1 == max_idx:
            if array[v-1] == x:
                print(1)
            else:
                print(0)
        else:
            print(1)

bs([-2,3,6,9,12],[-2,5,6,13])