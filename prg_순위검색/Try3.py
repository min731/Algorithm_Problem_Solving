def solution(info, query):
    answer = []

    # info 변환 Dict
    parser = {'-':-1,'cpp':0, 'java':1, 'python':2,
         'backend':0, 'frontend':1,
          'junior':0, 'senior':1,
          'chicken':0, 'pizza':1}

    par_inf = []

    # 변환
    for inf in info:
        
        inf = inf.split(" ")
        tmp_inf = []
        
        for i in range(4):
            tmp_inf.append(parser[inf[i]])
        tmp_inf.append(int(inf[-1]))

        par_inf.append(tmp_inf)

    # 이진 탐색 전 정렬
    par_inf = sorted(par_inf)

    print(par_inf)

    par_q = []

    # query 변환
    for q in query:
        q = q.replace("and","").split("  ")
        food_score = q[-1].split(" ")
        q[-1] = food_score[0]
        q.append(food_score[1])

        tmp_q = []

        for i in range(4):
            tmp_q.append(parser[q[i]])
        tmp_q.append(int(q[-1]))

        par_q.append(tmp_q)
    
    print(par_q)

    for q in par_q:
        print("-------------------------------")
        left = lowerbound(par_inf,q)
        right = upperbound(par_inf,q)

        tmp_inf = par_inf[left+1:right]

        print("tmp_inf : ",tmp_inf)
        print(" -- 점수 --")

        left , right = 0,len(tmp_inf)

        while left<right:
            
            mid = (left+right)//2
            print("left : ",left, " mid : ",mid, "right : ",right)
            if q[4] <= tmp_inf[mid][4] :
                right = mid
            else:
                if left < 0 :
                    break
                left = mid+1

            # print("left : ",left, " mid : ",mid, "right : ",right)

        ans_inf = tmp_inf[left:right+1]
        print("left : ",left," right : ",right)
        print("ans_inf : ",ans_inf )

        answer.append(right+1-left)

    print(answer)
    return answer

def lowerbound(par_inf, q):

    start, end = 0, len(par_inf)

    for i in range(4):
        print(i)
        if q[i] == -1:
            continue
        
        while start < end:
            mid = (start+end)//2
            print("q[i] <= par_inf[mid][i]",q[i] ,par_inf[mid][i])
            if q[i] <= par_inf[mid][i]:
                end=mid
            else:
                start=mid+1

            print("//start : ",start,", end :",end)

    return start

def upperbound(par_inf, q):

    start, end = 0, len(par_inf)

    for i in range(4):

        if q[i] == -1:
            continue
        
        while start < end:
            mid = (start+end)//2
            print("q[i] <= par_inf[mid][i]",q[i] ,par_inf[mid][i])
            if q[i] < par_inf[mid][i]:
                end=mid
            else:
                start=mid+1
        
            print("//start : ",start,", end :",end)
    
    return start

solution(

        ["java backend junior pizza 150",
          "python frontend senior chicken 210",
          "python frontend senior chicken 150",
          "cpp backend senior pizza 260",
          "java backend junior chicken 80",
          "python backend senior chicken 50"],

          ["java and backend and junior and pizza 100",
           "python and frontend and senior and chicken 200",
           "cpp and - and senior and pizza 250",
           "- and backend and senior and - 150",
           "- and - and - and chicken 100",
           "- and - and - and - 150"]

          )

[[0, 0, 1, 1, 260], [1, 0, 0, 0, 80], [1, 0, 0, 1, 150], [2, 0, 1, 0, 50], [2, 1, 1, 0, 150], [2, 1, 1, 0, 210]]
[[1, 0, 0, 1, 100], [2, 1, 1, 0, 200], [0, -1, 1, 1, 250], [-1, 0, 1, -1, 150], [-1, -1, -1, 0, 100], [-1, -1, -1, -1, 150]]