from itertools import product

def solution(word):
    answer = 0
    # print(3**4)
    alphabets  = ['A','E','I','O','U']
    
#     for i in range(5):
#         for j in range(1,6):
#             for k in product(alphabets[:j], repeat=j):
#                 print(k)
        
#         break
    
    # for i in range(1,6):
    #     for i in product(alphabets, repeat=i):
    #         print(j)
            
            

#     for i in range(len(alphabets)):
#         for 
        # alphabets[i]
        
    # for i in range(5):
    #     for 
    
    for i in product(alphabets, alphabets, alphabets):
        print(i, end=" ")

        

    return answer