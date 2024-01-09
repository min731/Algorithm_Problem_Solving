def available(n, times, t): # can evaluate n people within t time
    temp = 0
    for time in times:
        temp+= t//time
        if temp >=n:
            return 1
        else : 
            continue
    return 0

def solution(n, times):
    max_t = max(times)*n
    min_t = 1

    def search(min_t, max_t):
        # when will it return? 
        if ((max_t + min_t)//2 == min_t):
            if available(n, times, min_t):
                return min_t
            else:
                return max_t

        mid_t = (max_t + min_t)//2
        flag = available(n, times, mid_t)

        if flag == 1:
            return search(min_t, mid_t)
        else : # flag == 0
            return search(mid_t, max_t)

    return search(min_t, max_t)