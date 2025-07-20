from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    if not truck_weights:
        return 0
    
    waiting_trucks = deque(truck_weights)
    bridge = deque()  # (트럭무게, 나갈시간) 튜플로 저장
    
    current_weight = 0
    time = 0
    
    while waiting_trucks or bridge:
        time += 1
        
        # 다리에서 나갈 트럭이 있는지 확인
        if bridge and bridge[0][1] == time:
            _, exit_time = bridge.popleft()
            current_weight -= truck_weights[len(truck_weights) - len(waiting_trucks) - len(bridge) - 1]
        
        # 새 트럭이 들어갈 수 있는지 확인
        if waiting_trucks:
            next_truck = waiting_trucks[0]
            
            if current_weight + next_truck <= weight:
                truck = waiting_trucks.popleft()
                bridge.append((truck, time + bridge_length))
                current_weight += truck
    
    return time