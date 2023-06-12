def solution(picks, minerals):
    from collections import deque
    
    answer = 0
    
    # 다이아*돌 곡괭이로 모두 캘 때
    min_tired = 25*5*5
    
    # 문자 => 숫자
    
    for i in range(len(minerals)):
        if minerals[i] == "diamond":
            minerals[i] = 0
        elif minerals[i] == "iron":
            minerals[i] = 1
        else:
            minerals[i] = 2
    
    minerals = deque(minerals)
    stack = [[picks,minerals,0]]
    
    while stack:
        
        picks , minerals,tired = stack.pop()

        # print("곡괭이들 : ",picks)
        
        for i in range(len(picks)):
            # 다이아/철/돌 곡괭이 순서대로 캐기

            tmp_picks = picks
            tmp_minerals = minerals
            tmp_tired = tired

            if tmp_picks[i] > 0:
                tmp_picks[i] -= 1

                for _ in range(5):
                    if len(tmp_minerals) > 0 :
                        mineral = tmp_minerals.popleft()
                        if i <= mineral:
                            tmp_tired += 1
                        else:
                            tmp_tired += 5**(i-mineral)

                stack.append([tmp_picks,tmp_minerals,tmp_tired])
                print(stack)

        print("--------------------")
            
        print("곡괭이들 : ",picks)
        
        if sum(picks) == 0 or len(minerals) == 0:
            picks , mineral,tired = stack.pop()

            print("완료 picks , mineral,tired ",picks , mineral,tired)

            if tired < min_tired:
                min_tired = tired
        
    answer = min_tired
    
    print(answer)
    return answer


solution([1, 3, 2],["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"])
# solution([0, 1, 1],["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"])