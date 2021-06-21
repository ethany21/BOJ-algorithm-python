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
  
print(greed(parent, edges, count, answer))