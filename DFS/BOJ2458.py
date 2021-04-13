node, edge = map(int, input().split())
graph = [[0 for _ in range(node + 1)] for _ in range(node + 1)]

for _ in range(edge):
    low, high = map(int, input().split())
    graph[low][high] = 1

for k in range(node + 1):
    for i in range(node + 1):
        for j in range(node + 1):
            if graph[i][j] == 1 or(graph[i][k] + graph[k][j] == 2):
                graph[i][j] = 1
answer = 0
for i in range(node + 1):
    temp = 0
    for j in range(node + 1):
        temp += graph[i][j] + graph[j][i]
    if temp == node - 1:
        answer += 1
print(answer)