def solution(record):
    
    answer = []
    acts = {'Enter':0,'Leave':1,'Change':2}
    tmp = [] # 입장 : 0, 퇴장:1, 변경:2
    changes = {}
    
    for rec in record:

        rec = rec.split(" ")
        act, uid = rec[0], rec[1]

        if acts[rec[0]]==0 :
            tmp.append((acts[act],uid))
            name = rec[2]
            changes[uid] = name 
            
        elif acts[rec[0]]==1:
            tmp.append((acts[act],uid))
            
        else:
            name = rec[2]
            changes[uid] = name

    for x in tmp:
        act , uid = x
        if act==0:
            answer.append(changes[uid]+"님이 들어왔습니다.")
        else:
            answer.append(changes[uid]+"님이 나갔습니다.")

    return answer