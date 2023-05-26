def solution(n, words):
    
    answer = [0,0]
    wlist = []
    
    wlist.append(words[0])
        
    for i in range(0,len(words)-1):

        if words[i][-1] == words[i+1][0] :
            print(words[i][-1]+ "==" + words[i+1][0])
            
            # 중복O
            if words[i+1] in wlist:
                print(words[i+1] + "중복")
                answer[0] = (i+1) % n + 1 
                answer[1] = (i+1) //n + 1
                break
                
            # 중복X
            wlist.append(words[i+1])
        else :
            answer[0] = (i+1) % n + 1
            answer[1] = (i+1) //n + 1
            break
            

    return answer