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

        if 'OUT' not in data[number].keys():
            total_time += 1439-In[0]
            if total_time<=basic_time:
                answer.append(basic_fee)
            else:

                answer.append(int(basic_fee+math.ceil((total_time-basic_time)/per_time)*per_fee))
            continue

        # In = data[number]['IN']
        Out = data[number]['OUT']

        while Out:

            v_in = In.popleft()
            v_out = Out.popleft()
            
            total_time += v_out-v_in

        if In:
            total_time += 1439-In[0]
        
        if total_time<=basic_time:
            answer.append(basic_fee)
        else:

            answer.append(int(basic_fee+math.ceil((total_time-basic_time)/per_time)*per_fee))

    return answer