def solution(n):
    result=[]
    sum=0
    while n!=0:
        result.append(n%3)
        n=n//3
    for i in range(len(result)):
        sum=sum+((3**(len(result)-i-1))*result[i])
        
    return sum