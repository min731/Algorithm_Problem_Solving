def find_parent(parent,x):
    
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
        
    return parent[x]

def union_parent(parent,start,end):
    
    start = find_parent(parent,start)
    end = find_parent(parent,end)

    if start<end:
        parent[end] = start
    else:
        parent[start] = end
    
def solution(n,costs):
    
    answer = 0
    
    islands = [i for i in range(n)]
    # print(islands)
    
    costs = sorted(costs, key=lambda x:x[2])
    print("costs : ",costs)
    
    for cost in costs:
        start,end,fee = cost
        print("islands : ",islands)
        print("start : ",start, " end : ",end)
        # start 와 end는 모두 연결이 가능
        # but, 부모가 다르면 크루스칼 연결이 안된 상태 => 어느 한쪽에 속하게 해야함
        if find_parent(islands,start) != find_parent(islands,end):
            print("if")
            union_parent(islands,start,end)
            answer += fee
        
    return answer