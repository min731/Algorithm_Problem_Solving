def solution(fees, records):
    answer = []

    basic_time = fees[0]
    basic_fee = fees[1]
    per_time = fees[2]
    per_fee = fees[3]

    data = {}

    for record in records:
        record = record.split()

        time = record[0]
        # num = record[1]
        inOut = record[2]

        print(record)

        # 05:34 5961 IN
        if record[1] not in data.keys():
            data[record[1]] = {}

        if record[2] not in data[record[1]].keys():
            data[record[1]][record[2]] = []

        data[record[1]][record[2]].append(record[0]) 
        
        print(data)

        # if record[2] not in data[record[1]][record[2]].keys():
        #     data[record[1]][record[2]] = {}
        # data[record[1]][record[2]] = record[0]

    # for 

    print(data)
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