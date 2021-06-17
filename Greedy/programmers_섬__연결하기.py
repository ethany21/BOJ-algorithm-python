def solution(n, costs):
    answer = 0
    
    maximum = max(costs, key = lambda x: x[2])[2]
    
    graph = [[maximum + 1 for _ in range(n)] for _ in range(n)]
    
    for i in costs:
        graph[i[0]][i[1]] = i[2]
        graph[i[1]][i[0]] = i[2]
    
    
    
    return answer