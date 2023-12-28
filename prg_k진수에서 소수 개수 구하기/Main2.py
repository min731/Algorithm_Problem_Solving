def k_jinsoo(k,n):
    
    now = 1
    m = 13
    jinsoo = ''
    rest = n
    
    for i in range(m-1,-1,-1):
        # print(i,n,k**i)
        share, rest = divmod(rest,k**i)
        jinsoo += str(share)

    print(k,"진수", jinsoo)
    
    return jinsoo
    
def solution(n, k):
    answer = 0
    global jinsoo
    
    jinsoo = ''
    
    jinsoo = k_jinsoo(k,n)
    
    # print(jinsoo)
    
    jinsoo = jinsoo.split("0")
    print(jinsoo)
    
    Primes = set()
    
    for x in jinsoo:
        if x == "" or x == "1":
            continue
        else:
            x = int(x)
            
            if x in Primes:
                answer += 1
                continue
            else:
                # print(x)
                isPrime = True
                for i in range(2,x):
                    # print(i)
                    if x%i==0:
                        isPrime = False
                        break
                # print(isPrime,x)
                if isPrime:
                    Primes.add(x)
                    answer += 1

    return answer