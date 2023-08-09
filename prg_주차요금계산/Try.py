def solution(fees, records):

    from collections import deque

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

        print(record)

        # 05:34 5961 IN
        if num not in data.keys():
            data[num] = {}

        if inOut not in data[num].keys():
            data[num][inOut] = deque([])

        data[num][inOut].append(time) 
        
        print(data)

        # if record[2] not in data[record[1]][record[2]].keys():
        #     data[record[1]][record[2]] = {}
        # data[record[1]][record[2]] = record[0]
    print(data)

    numbers = sorted(data.keys())
    print(numbers)

    for number in numbers:

        total_time = 0

        In = data[number]['IN']
        Out = data[number]['OUT']

        while Out:
            
            print("In : ",In)
            print("Out : ",Out)

            v_in = In.popleft()
            v_out = Out.popleft()
            
            if v_out == None:
                total_time += 1439-v_in
            else:
                total_time += v_out-v_in
        
        answer.append(5000+(total_time-basic_time)/per_time*per_fee)

    print(answer)
    return answer

solution([180, 5000, 10, 600],["05:34 5961 IN", 
                               "06:00 0000 IN", 
                               "06:34 0000 OUT", 
                               "07:59 5961 OUT", 
                               "07:59 0148 IN", 
                               "18:59 0000 IN", 
                               "19:09 0148 OUT", 
                               "22:59 5961 IN", 
                               "23:00 5961 OUT"])