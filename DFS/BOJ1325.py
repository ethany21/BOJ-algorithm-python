node, edge = map(int, input().split())

graph = []
for _ in range(edge):
    graph.append(list(map(int, input().split())))
    
dic = {}

for i in range(1, node+1):
    # dic[i] = 1
    dic[i] = [i]

def dfs(graph, first, original):
    visited = [False for _ in range(edge)]
    count = 0
    for i in visited:
        if i == True:
            count += 1
    if count == len(visited):
        return

    for i in range(edge):
        if graph[i][1] == first and not visited[i]:

            dic[original].append(graph[i][0])
            # dic[original] += 1
            first = graph[i][0]
            visited[i] = True
            dfs(graph, first, original)
            first = graph[i][1]
            visited[i] = False

for i in range(1, node+1):
    dfs(graph, i, i)

max = 0
for i in dic.keys():
    if len(dic[i]) > max:
        max = len(dic[i])

answer = []

for i in dic.keys():
    if len(dic[i]) == max:
        answer.append(i)
answer.sort()
for i in answer:
    print(i, end=' ')