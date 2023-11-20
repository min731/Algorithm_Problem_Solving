def dfs(cnt, w,words,word_list):
    # print(w)
    # if w == 'EEEEE':
    #     exit()
    if cnt == 5:
        return 
    for i in range(len(words)):
        word_list.append(w + words[i])
        dfs(cnt+1, w + words[i],words,word_list)

def solution(word):
    answer = 0
    word_list = []
    words = 'AEIOU'
            
    dfs(0,"",words,word_list)
    
    print(word_list.index(word)+1)
    return word_list.index(word)+1

#solution("AAAAA")

arr = [[1,2,3],
[4,5,6], 
[7,8,9]]
# print(zip(arr))
print(*arr[0])

for i in zip(arr):
    print(i)

arr = list([i[::-1] for i in zip(*arr)])[::-1]
# print(arr)
for y in arr:
    for x in y:
        print(x,end = ' ')
    print()
