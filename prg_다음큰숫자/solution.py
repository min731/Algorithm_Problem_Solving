def solution(n):
    
    for i in range(n+1,1000001):
        if str(bin(i)[2:].count('1')) == str(bin(n)[2:].count('1')):
            answer = i
            break;
    return answer