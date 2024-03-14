def down(n,x,y,v,arr):
    
    if x+1<n and arr[x+1][y]!=-1:
        return False,x,y,v,arr
    
    while x+1<n and arr[x+1][y]==-1:
        v += 1
        arr[x+1][y] = v
        x += 1
        
    return True,x,y,v,arr
    
def right(n,x,y,v,arr):

    if y+1<n and arr[x][y+1]!=-1:
        return False,x,y,v,arr
    
    while y+1<n and arr[x][y+1]==-1:
        v += 1
        arr[x][y+1] = v
        y += 1

    return True,x,y,v,arr

def left_up(n,x,y,v,arr):
    
    if x-1<n and y-1<n and arr[x-1][y-1]!=-1:
        return False,x,y,v,arr
    
    while x-1<n and arr[x-1][y-1]==-1:
        v += 1
        arr[x-1][y-1] = v
        x -= 1
        y -= 1

    return True,x,y,v,arr

def solution(n):
    
    if n==1:
        return [1]
    
    answer = []
    arr = [[-1 for i in range(n)] for j in range(n)]
    
    x = 0
    y = 0
    v = 1
    arr[x][y] = v

    while True:
        d_isContinue,x,y,v,arr = down(n,x,y,v,arr)
        if not d_isContinue:
            break
        r_isContinue,x,y,v,arr = right(n,x,y,v,arr)
        if not r_isContinue:
            break
        lu_isContinue,x,y,v,arr = left_up(n,x,y,v,arr)
        if not lu_isContinue:
            break
        # if d_isContinue==False or r_isContinue==False or lu_isContinue==False:
        #     break

    for line in arr:
        for x in line:
            if x!=-1:
                answer.append(x)
    
    return answer

solution(2)
# print(False or False or True)