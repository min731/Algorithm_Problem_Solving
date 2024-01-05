def solution(land):
    answer = 0

    scores = {str(idx):score for idx,score in enumerate(land[0])}
    print(scores)
    now_x = 0
    max_x = len(land)-1
    
    while now_x<max_x:
        # print("--------------")
        now_x += 1
        tmp_scores = {}

        for new_idx, new_score in enumerate(land[now_x]):
            for now_idx, now_score in scores.items():
                if str(new_idx) != now_idx[-1]:
                    tmp_scores[now_idx+str(new_idx)] = now_score+new_score
        scores = tmp_scores
    
    for k,v in scores.items():
        # print(k,v)
        if v>answer:
            answer = v
    
    
    return answer