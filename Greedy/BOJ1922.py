n = int(input())
edge = int(input())
graph = []
for _ in range(edge):
    graph.append(list(map(int, input().split())))

graph = sorted([[x[2], x[1], x[0]] for x in graph ])
answer = 0
count = 0
parent =[i for i in range(n)]

def ancestor(parent, node):
    if parent[node] == node:
        return node
    else:
        return ancestor(parent, parent[node])

for cost, end, start in graph:
    if ancestor(parent, end-1) != ancestor(parent, start-1):
        answer += cost
        count += 1
        parent[ancestor(parent, start-1)] = end-1
    if count  == n - 1:
        break
print(answer)