from collections import deque
def get_hap_list(arr):
    
    hap_list = []
    tmp = 0
    for i in range(len(arr)):
        hap_list.append(tmp+arr[i])
        tmp += arr[i]
    
    return hap_list

def solution(queue1, queue2):
    answer = -2
    half = len(queue1)
    max_chance = len(queue1)*2-1
    chance = 0
    target = sum(queue1+queue2)/2

    while chance<=max_chance:
        print("----------------------------")
        # print("queue : ",queue)
        # print("hap_list : ",hap_list)
        len1 = len(queue1)
        len2 = len(queue2)        
        print(queue1+queue2)
        queue = queue1+queue2

        hap_list = get_hap_list(queue)
        print("hap_list : ",hap_list)
        start = 0
        end = len(queue)-1    

        while start<end:
            mid = (start+end)//2
            hap1 = hap_list[mid]
            hap2 = hap_list[end]-hap_list[mid]
            
            if hap1==target and hap1==hap2:
                print("chance : ",chance)
                print("mid : ",mid)
                answer = chance+abs(half-mid)
                print("answer : ",answer)
                return
            elif hap1<target:
                start = mid+1
            else:
                end = mid-1

        chance += 1
        queue2 = queue2.append(queue1[-1])
        queue1 = queue1[1:]
        # queue2 = queue2.append(queue1[-1])

    # print(answer)
    answer = -1
    print(answer)
    return answer

solution([3, 2, 7, 2],[4, 6, 5, 1])
# solution([1, 2, 1, 2],[1, 10, 1, 2])
# solution([1, 1],[1, 5])

