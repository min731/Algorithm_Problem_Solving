def solution(picks, minerals):
    from collections import deque
    import copy
    
    answer = 0
    
    # 다이아*돌 곡괭이로 모두 캘 때
    min_tired = 50*25
    
    # 문자 => 숫자
    
    for i in range(len(minerals)):
        if minerals[i] == "diamond":
            minerals[i] = 0
        elif minerals[i] == "iron":
            minerals[i] = 1
        else:
            minerals[i] = 2
    
    minerals = deque(minerals)
    queue = deque([[picks,minerals,0]])
    
    while queue:
        
        picks , minerals,tired = queue.popleft()

        # print("곡괭이들 : ",picks)
        
        for i in range(len(picks)):
            # 다이아/철/돌 곡괭이 순서대로 캐기

            tmp_picks = copy.deepcopy(picks)
            tmp_minerals = copy.deepcopy(minerals)
            tmp_tired = copy.deepcopy(tired)

            if tmp_picks[i] > 0:
                tmp_picks[i] -= 1

                for _ in range(5):
                    if len(tmp_minerals) > 0 :
                        mineral = tmp_minerals.popleft()
                        if i <= mineral:
                            tmp_tired += 1
                        else:
                            tmp_tired += 5**(i-mineral)

                queue.append([tmp_picks,tmp_minerals,tmp_tired])
                print(queue)
                if sum(tmp_picks) == 0 or len(tmp_minerals) == 0:
                    picks , mineral,tired = queue.pop()

                    print("완료 picks , mineral,tired ",tmp_picks , tmp_minerals,tmp_tired)

                    if tmp_tired < min_tired:
                        min_tired = tmp_tired

        print("--------------------")
        
    answer = min_tired
    
    print(answer)
    return answer


solution([1, 3, 2],["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"])
# solution([0, 1, 1],["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"])