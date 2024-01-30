def find_parent(parent,x):
    
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
        
    return parent[x]

def union_parent(parent, start, end):
    start_p = find_parent(parent,start)
    end_p = find_parent(parent,end)
    
    if start_p<end_p:
        parent[end_p] = start_p
    else:
        parent[start_p] = end_p

def solution(n,costs):
    
    answer = 0
    parent = [i for i in range(n)]
    costs = sorted(costs, key=lambda x:x[2])
    # length = len(costs)
    
    for case in costs:
        start, end , cost = case
        # print("---------------------")
        # print("start : ", start, " end : ",end, "cost : ",cost)
        # print("parent : ",parent)
        
        if find_parent(parent,start) != find_parent(parent,end):
            union_parent(parent,start,end)
            answer += cost
            
    return answer