def convert(cnt_zero,s):
    
    cnt_zero_now = 0
    s = list(s)
    
    org_len = len(s)

    for i in range(org_len):

        if s[i] == '0':
            s[i] = ""
            cnt_zero += 1
            cnt_zero_now += 1
    
    return cnt_zero , "{0:b}".format(org_len-cnt_zero_now)

def solution(s):
    
    cnt = 0
    cnt_zero = 0
    check = True
    
    while check:

        bh_s = s
        cnt_zero,s = convert(cnt_zero,s)
        aft_s = s
        
        if bh_s == aft_s :
            check = False
        else:
            cnt += 1
    answer = []
    answer.append(cnt)
    answer.append(cnt_zero)
    
    return answer