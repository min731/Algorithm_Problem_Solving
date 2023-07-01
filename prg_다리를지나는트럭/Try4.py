def solution(bridge_length, weight, truck_weights):
    from collections import deque
    
    answer = 0

    # bridge = deque([0 for _ in range(bridge_length)])
    trucks = deque(truck_weights)
    bridge = {}

    bridge[trucks.popleft()] = bridge_length

    print(bridge)

    cnt = 1
    
    # print(sum(bridge.values()))

    while sum(bridge.values()) != 0:

        print("--------------")

        now_weights = 0

        for key in bridge.keys():
            if bridge[key] != 0:
                now_weights += key

        if len(trucks) > 0 :
        
        # truck = trucks.popleft()
            if now_weights+trucks[0]<=weight:
                truck = trucks.popleft()
                bridge[truck] = bridge_length

        for key in bridge.keys():
            bridge[key] -= 1

        cnt += 1
        
        print("trucks : ",trucks)
        print("bridge : ",bridge)

    answer = cnt
    print("answer : ",answer)
    return answer


solution(2,10,[7,4,5,6])
solution(100,100,[10])
# solution(100,100,[10,10,10,10,10,10,10,10,10,10])
