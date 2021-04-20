from itertools import combinations
from collections import deque

# N, M = map(int, input().split())

graph = []
count = 0
cands = []
cords = []

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


for _ in range(M):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            count += 1
            cords.append([i, j])


cands = list(combinations(cords, 3))

for comb in range(cands):

    queue = deque()

    for cord in comb:
        graph[cord[0]][cord[1]] = 1

    while queue:
        
    




