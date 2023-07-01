def solution(bridge_length, weight, truck_weights):
    from collections import deque
    
    answer = 0

    bridge = [0 for _ in range(bridge_length)]

    bridge[-1] = truck_weights.pop(0)

    print(bridge)

    cnt = 1

    while bridge:

        print("--------------")
        bridge.pop(0)

        if truck_weights:
        
            if sum(bridge)+truck_weights[0]<=weight:
                truck = truck_weights.pop(0)
                bridge.append(truck)
            else:
                
                bridge.append(0)

        cnt += 1
        
        print("trucks : ",truck_weights)
        print("bridge : ",bridge)

    answer = cnt
    print("answer : ",answer)
    return answer


solution(2,10,[7,4,5,6])
# solution(100,100,[10])
# solution(100,100,[10,10,10,10,10,10,10,10,10,10])
