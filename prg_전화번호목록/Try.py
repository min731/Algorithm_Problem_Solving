from collections import deque

def binary_search(now,queue):
    
    start = 0
    end = len(queue)
    now_len=len(now)
    
    while start<end:
        
        mid = (start+end)//2
        print("start : ",start," end : ",end, " mid : ",mid)
        print("queue[mid] : ",queue[mid])
        
        if now_len<=len(queue[mid]):
            if now == queue[mid][:now_len]:
                return False
            else:
                start = mid
        elif now_len>len(queue[mid]):
            end = mid
    
    return True
    
def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    queue = deque(phone_book)
    print(queue)
    
    while queue:
        
        print("--------------")
        now = queue.popleft()
        print("now : ",now)
        answer = binary_search(now,queue)
        if not answer:
            break
            
    return answer

solution(["119", "97674223", "1195524421"])