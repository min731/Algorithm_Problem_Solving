from collections import deque

def solution(begin, target, words):
    answer = 0

    if target not in words:
        answer = 0

        print("answer : ",answer)
        return answer

    queue = deque([(begin,0)])
    print("queue : ",queue)

    while queue:

        print("------------------------")
        print("queue : ",queue)

        now_word,cnt = queue.popleft()

        if now_word == target:
            answer = cnt
            break
        else:
            queue.extend(get_queue(now_word,cnt,words))
        
    print("answer : ",answer)
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


solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"])
solution("hit","cog",["hot", "dot", "dog", "lot", "log"])