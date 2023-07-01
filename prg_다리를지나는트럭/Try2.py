def solution(bridge_length, weight, truck_weights):
    from collections import deque
    
    answer = 0

    # bridge = deque([0 for _ in range(bridge_length)])
    trucks = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])

    bridge[-1] = trucks.popleft()

    print(bridge)

    cnt = 1

    while sum(bridge) != 0:

        print("--------------")
        crossed = bridge.popleft()

        if len(trucks) > 0 :
        
        # truck = trucks.popleft()
            if sum(bridge)+trucks[0]<=weight:
                truck = trucks.popleft()
                bridge.append(truck)
            else:
                
                bridge.append(0)
        else:
            bridge.append(0)

        cnt += 1
        
        print("trucks : ",trucks)
        print("bridge : ",bridge)

    answer = cnt
    print("answer : ",answer)
    return answer


# solution(2,10,[7,4,5,6])
# solution(100,100,[10])
solution(100,100,[10,10,10,10,10,10,10,10,10,10])
