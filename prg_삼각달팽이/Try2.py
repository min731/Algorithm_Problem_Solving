def down(n,x,y,v,arr):
    
    while x+1<n and arr[x+1][y]==-1:
        v += 1
        arr[x+1][y] = v
        x += 1
    
    if arr[x-1][y]!=-1:
        return False,x,y,v,arr
    
    return True,x,y,v,arr
    
def right(n,x,y,v,arr):
    
    while y+1<n and arr[x][y+1]==-1:
        v += 1
        arr[x][y+1] = v
        y += 1
    
    if arr[x][y-1]!=-1:
        return False,x,y,v,arr
    
    return True,x,y,v,arr

def left_up(n,x,y,v,arr):
    
    while x-1<=n and arr[x-1][y-1]==-1:
        v += 1
        arr[x-1][y-1] = v
        x -= 1
        y -= 1

    if arr[x+1][y+1]!=-1:
        return False,x,y,v,arr
    
    return True,x,y,v,arr

def solution(n):
    answer = []
    arr = [[-1 for i in range(n)] for j in range(n)]
    
    for line in arr:
        print(line)
    
    # print(len(arr))
    # print(len(arr[0]))
    x = 0
    y = 0
    v = 1
    arr[x][y] = v
    isContinue = True
    
    while True:
        isContinue,x,y,v,arr = down(n,x,y,v,arr)
        if not isContinue:
            break
        isContinue,x,y,v,arr = right(n,x,y,v,arr)
        if not isContinue:
            break
        isContinue,x,y,v,arr = left_up(n,x,y,v,arr)
        if not isContinue:
            break

#     isContinue = False
    
#     while True:
#         isContinue = check(x,y,v,arr)
        
        
#         if not isContinue:
#             break
    print("-------------------------")
    for line in arr:
        print(line)
    
    arr = arr
    print(arr)
    
    return answer