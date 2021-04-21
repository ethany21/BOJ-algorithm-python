from itertools import combinations
from collections import deque

N, M = map(int, input().split())

graph = []
count = 0
cands = []
cords = []
walls = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


for _ in range(M):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            count += 1
            cords.append([i, j])
        elif graph[i][j] == 2:
            walls.append([i, j])

cands = list(combinations(cords, 3))
answers = [count for _ in range(len(cands))]

for comb in range(cands):

    queue = deque(walls)

    for cord in comb:
        graph[cord[0]][cord[1]] = 1

    while queue:
        temp = []
        while len(queue) > 0:
            temp.append(queue.popleft())
        for hue in temp:
            a, b = hue[0], hue[1]
            for i in range(4):
                x = a + dx[i]
                y = b + dy[i]
                if 0 <= x < N and 0 <= y < M and graph[x][y] == 0:
                    queue.append([x,y])
                    answers[comb] -=1
                    graph[x][y] = 2
        
    




