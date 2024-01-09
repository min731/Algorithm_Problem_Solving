def solution(n, times):
    
    answer = -1
    gates = {str(time):0 for time in times}
    
    print(gates)
    
    while n>-2:
        answer += 1

        print("---------------------")
        tmp_gates = []
        # print("gates : ",gates)
        for gate,rest in gates.items():
            if gates[gate]==0: 
                tmp_gates.append(gate)
                n -= 1
        tmp_gates.sort(reverse=True)
        print("tmp_gates : ", tmp_gates)
        
        for tmp_gate in tmp_gates:
            gates[tmp_gate] = int(tmp_gate)
            # n -= 1

        for gate,rest in gates.items():
            gates[gate] -= 1
        
        print("gates : ",gates)
        print("answer :",answer)
        print("n : ",n)

    return answer 

solution(6,[7, 10])