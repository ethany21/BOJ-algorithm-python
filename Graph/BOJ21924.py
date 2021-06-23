n, edge = map(int, input().split())

graph =[]
total = 0
for _ in range(edge):
    x,y, cost = map(int, input().split())
    graph.append([x,y,cost])
    total += cost

parent = [i for i in range(n +1)]
edges = sorted([(x[2], x[1], x[0]) for x in graph])
count = 0
answer = 0

def ancestor(parent, x):
    result = x
    while parent[result] != result:
        result = parent[result]
    parent[x] = result
    return parent[x]

def union_find(x, y):
    X = ancestor(parent, x)
    Y = ancestor(parent, y)
    if X == Y:
        return False
    parent[X] = Y
    return True

def greed(edges, answer):
    for node in edges:
        cost, start, end = node
        if union_find(start, end):
            answer += cost
    
    return total - answer
print(greed(edges, answer))
print(parent)
for i in range(n):
    if i == parent[i]:
        count +=1
print(count)

# if check_link(check):
#     print(greed(parent, edges, count, answer))
# else:
#     print(-1)