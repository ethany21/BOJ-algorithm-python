n, edge = map(int, input().split())

graph =[]
total = 0
for _ in range(edge):
    graph.append(list(map(int, input().split())))

for i in range(len(graph)):
    total += graph[i][-1]

parent = [i for i in range(n)]
edges = sorted([(x[2], x[1], x[0]) for x in graph])
count = 0
answer = 0
visited = [0 for i in range(n + 1)]
check = 0

another = [[0 for _ in range(1+n)] for _ in range(n+1)]
for i in range(len(graph)):
    a, b, c = graph[i]
    another[a][b] = 1
    another[b][a] = 1


def dfs(i):
    visited[i] = 1
    for j in range(1, n+1):
        if another[i][j] == 1 and visited[j] == 0:
            dfs(j)

def check_link(check):
    for i in range(1, n+1):
        if visited[i] != 1:
            dfs(i)
            check +=1
    if check != 1:
        return False
    else:
        return True

def ancestor(parent, node):
    if parent[node] == node:
        return node
    else:
        return ancestor(parent, parent[node])

def greed(parent, edges, count, answer):
    for node in edges:
        cost, start, end = node
        if ancestor(parent, start-1) != ancestor(parent, end-1):
            count += 1
            answer += cost
            parent[ancestor(parent, end-1)] = start-1
        if count == n-1:
            break
    
    return total - answer

if check_link(check):
    print(greed(parent, edges, count, answer))
else:
    print(-1)