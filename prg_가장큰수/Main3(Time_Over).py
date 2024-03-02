from collections import deque

def solution(numbers):
    answer = '0'
    
    tmp = numbers
    queue = deque([['',0,[-1]]])
    
    while queue:
    
        v,cnt,hist = queue.popleft()
        print("------------------")
        print("queue : ",queue)
        print(v,cnt,hist)

        if cnt==len(numbers):
            print("break!!")
            if v>answer:
                answer = v
            continue
        
        for i,x in enumerate(tmp):
            if i not in hist:
                queue.append([v+str(x),cnt+1,hist+[i]])
        
    # print(queue)
    # answer = sorted(queue, key=lambda x:x[0])[-1][0]
    print(answer)
    return  answer

solution([6, 10, 2])
# solution([3, 30, 34, 5, 9])
# solution([9,997])