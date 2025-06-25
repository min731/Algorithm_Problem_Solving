def solution(arr):
    ans = []
    last = -1
    
    for i in range(len(arr)):
        
        if last!=arr[i]:
            ans.append(arr[i])
            last = arr[i]
    
    return ans