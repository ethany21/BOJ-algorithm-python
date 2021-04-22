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


for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            count += 1
            cords.append([i, j])
        elif graph[i][j] == 2:
            walls.append([i, j])



cands = list(combinations(cords, 3))
answers = [0 for _ in range(len(cands))]

for comb in range(len(cands)):
    
    queue = deque()
    for i in walls:
        queue.append(i)
    
    box = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            box[i][j] = graph[i][j]

    for cord in cands[comb]:
        box[cord[0]][cord[1]] = 1

    while queue:
        temp = []
        while len(queue) > 0:
            temp.append(queue.popleft())
        for hue in temp:
            a, b = hue[0], hue[1]
            for i in range(4):
                x = a + dx[i]
                y = b + dy[i]
                if 0 <= x < N and 0 <= y < M and box[x][y] == 0:
                    queue.append([x,y])
                    box[x][y] = 2
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                answers[comb] += 1
print(max(answers))