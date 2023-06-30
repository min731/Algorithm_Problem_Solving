from collections import deque

def solution(n, info):
    answer = []

    # 갱신되는 라이언-어피치 값
    answer_val=0
    dq=deque()

    # dq(과녁포인터,[점수별 화살갯수])
    dq.append((0, [0,0,0,0,0,0,0,0,0,0,0]))
    
    while dq:

        print("---------------")

        # focus : 과녁 포인터
        # arrow : 화살 분포
        focus, arrow = dq.popleft()

        # 화살 다썼는지 확인
        cnt=n-sum(arrow)
        
        # 지나치게 다쓰면 제외
        if cnt<0:
            continue

        # 딱 알맞게 쓰면 점수 계산
        if cnt==0 or focus>=10:
            arrow[10]=cnt
            lion=0
            apeach=0
            for i in range(10):
                if arrow[i]>info[i]:
                    lion+=10-i
                elif info[i]>0:
                    apeach+=10-i
            if lion>apeach:
                if answer_val<=lion-apeach:
                    answer_val=lion-apeach
                    answer=arrow.copy()
            continue
        
        # 어피치의 점수에 종속되어 해당 점수에 화살+1개
        arrow[focus]=info[focus]+1
        dq.append((focus+1, arrow.copy()))

        # 현재 focus에 화살을 빼고 다음 foucus에 분배
        arrow[focus]=0
        dq.append((focus+1, arrow.copy()))

        print(dq)
        
        if len(dq) == 70:
            break

    if sum(answer)==0:
        answer.append(-1)
    return answer

solution(5,[2,1,1,1,0,0,0,0,0,0,0])