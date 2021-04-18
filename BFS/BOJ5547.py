N, M = map(int, input().split())

graph = []
cord = []
answer = 0

for _ in range(M):
    graph.append(list(map(int, input().split())))

for i in range(1, M+1):
    temp = []
    for j in range(1, N+1):
        temp.append([j, i])
    cord.append(temp)

