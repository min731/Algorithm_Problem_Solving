def solution(fees, records):

    from collections import deque
    import math

    answer = []

    basic_time = fees[0]
    basic_fee = fees[1]
    per_time = fees[2]
    per_fee = fees[3]

    data = {}


    for record in records:
        record = record.split()

        time = record[0]
        time = time.split(':')
        time = int(time[0])*60+int(time[1])

        num = record[1]
        inOut = record[2]

        # 05:34 5961 IN
        if num not in data.keys():
            data[num] = {}

        if inOut not in data[num].keys():
            data[num][inOut] = deque([])

        data[num][inOut].append(time) 

    numbers = sorted(data.keys())

    for number in numbers:

        total_time = 0
        
        In = data[number]['IN']

        only_IN = 0
        if 'OUT' not in data[number].keys():
            only_IN = True
            total_time += 1439-In[0]
            break

        # In = data[number]['IN']
        Out = data[number]['OUT']

        while Out:

            v_in = In.popleft()
            v_out = Out.popleft()
            
            total_time += v_out-v_in

        if In:
            total_time += 1439-In[0]
        
        print("total_time : ", total_time )
        if total_time<=basic_time:
            answer.append(basic_fee)
        else:

            answer.append(int(basic_fee+math.ceil((total_time-basic_time)/per_time)*per_fee))

    if only_IN:
        if total_time<=basic_time:
            answer.append(basic_fee)
        else:

            answer.append(int(basic_fee+math.ceil((total_time-basic_time)/per_time)*per_fee))

    print("total_time : ",total_time)
    print(only_IN)
    print(answer)
    return answer

# solution([180, 5000, 10, 600],["05:34 5961 IN", 
#                                "06:00 0000 IN", 
#                                "06:34 0000 OUT", 
#                                "07:59 5961 OUT", 
#                                "07:59 0148 IN", 
#                                "18:59 0000 IN", 
#                                "19:09 0148 OUT", 
#                                "22:59 5961 IN", 
#                                "23:00 5961 OUT"])

solution([120, 0, 60, 591],["16:00 3961 IN",
                            "16:00 0202 IN",
                            "18:00 3961 OUT",
                            "18:00 0202 OUT",
                            "23:58 3961 IN"])

# solution([1, 461, 1, 10],["00:00 1234 IN"])