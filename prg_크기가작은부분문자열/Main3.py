def solution(t, p):
    idx=len(p)
    arr=[]
    cnt=0
    for i in range(len(t)-idx+1):
        arr.append(t[i:i+idx])
        
    for i in range(len(arr)):
        if int(arr[i])<=int(p):
            cnt+=1

    answer = cnt
    return answer