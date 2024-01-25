import heapq

def solution(jobs):
    answer = 0
    
    length = len(jobs)
    # jobs = sorted(jobs, key=lambda x:x[1])
    jobs = [[x[1],x[0]] for x in jobs]
    heapq.heapify(jobs)
    print(jobs)
    # prior_point = 0
    now = 0
    
    while jobs:
        
        # print("-----------")
        time, point = heapq.heappop(jobs)
        # print(job)
        # print("point : ",point, " time : ",time, "answer : ",answer)
        # now += time
        if now<=point:
            answer += time
            now += time
        else:
        # now += time
            now += time
            answer += now-point
        
        print("point : ",point, " time : ",time, "now :", now, "answer : ",answer)        
        # answer += (now-point)
        
        # prior_point = point
        
    answer /= length
    answer = int(answer)
    return answer