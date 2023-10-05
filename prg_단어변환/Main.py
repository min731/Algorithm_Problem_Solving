from collections import deque

def solution(begin, target, words):
    answer = 0

    if target not in words:
        answer = 0

        return answer

    queue = deque([(begin,0)])

    while queue:

        now_word,cnt = queue.popleft()

        if now_word == target:
            answer = cnt
            break
        else:
            queue.extend(get_queue(now_word,cnt,words))
        
    return answer

def get_queue(now_word,cnt,words):

    queue = deque([])
    for word in words:
        wrong = 0
        can_convert = True
        for idx,x in enumerate(word):
            if x!=now_word[idx]:
                wrong += 1
            if wrong == 2:
                can_convert = False
                break
        if can_convert:
            queue.append((word,cnt+1))
    
    return queue