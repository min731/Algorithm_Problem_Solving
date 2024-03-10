def solution(a, b):
    answer = ''
    yoil = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    # print(days[:a-1])
    
    answer = yoil[(sum(days[:a-1])+b)%7-1]
    return answer