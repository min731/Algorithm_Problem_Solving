def down(n,x,y,v,arr):
    
    while x+1<n and arr[x+1][y]==-1:
        v += 1
        arr[x+1][y] = v
        x += 1
        
    return x,y,v,arr
    
def right(n,x,y,v,arr):
    
    while y+1<n and arr[x][y+1]==-1:
        v += 1
        arr[x][y+1] = v
        y += 1
    
    return x,y,v,arr

def left_up(n,x,y,v,arr):
    
    while x-1<=n and arr[x-1][y-1]==-1:
        v += 1
        arr[x-1][y-1] = v
        x -= 1
        y -= 1
        
    return x,y,v,arr

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
    
    x,y,v,arr = down(n,x,y,v,arr)
    x,y,v,arr = right(n,x,y,v,arr)
    x,y,v,arr = left_up(n,x,y,v,arr)
    
    
#     isContinue = False
    
#     while True:
#         isContinue = check(x,y,v,arr)
        
        
#         if not isContinue:
#             break
    print("-------------------------")
    for line in arr:
        print(line)

    return answer