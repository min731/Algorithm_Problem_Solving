def solution(bridge_length, weight, truck_weights):
    from collections import deque
    
    answer = 0

    # bridge = deque([0 for _ in range(bridge_length)])
    trucks = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])

    bridge[-1] = trucks.popleft()

    sum_bridge = sum(bridge)

    cnt = 1

    while bridge:

        print("--------------")
        crossed = bridge.popleft()

        if trucks:
            
            print("sum : ",sum_bridge,"crossed : ",crossed,"trucks[0] : ",trucks[0])
            sum_bridge -= crossed
            sum_bridge += trucks[0]
            
            print("sum : ",sum_bridge)
        
            if sum_bridge<=weight:
                truck = trucks.popleft()
                bridge.append(truck)
            else:
                sum_bridge -= trucks[0]
                bridge.append(0)

        cnt += 1
        
        print("trucks : ",trucks)
        print("bridge : ",bridge)

    answer = cnt
    print("answer : ",answer)
    return answer


solution(2,10,[7,4,5,6])
# solution(100,100,[10])
# solution(100,100,[10,10,10,10,10,10,10,10,10,10])
