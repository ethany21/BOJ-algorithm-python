node, edge = map(int, input().split())

graph = []
for _ in range(edge):
    graph.append(map(int, input().split()))
    
dic = {}

def dfs(graph, first):
    visited = [False for _ in range(edge)]
    count = 0
    for i in visited:
        if i == True:
            count += 1
    if count == len(visited):
        return

    for i in range(edge):
        if graph[i][1] == first and not visited[i]:
            
            

            first = graph[i][0]
            visited[i] = True
            dfs(graph, first)
