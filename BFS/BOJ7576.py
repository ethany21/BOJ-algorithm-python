import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())

box = []
for _ in range(N):
    box.append(list(map(int, sys.stdin.readline().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

target = 0
queue = deque()
answer = 0
count = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            target +=1
        elif box[i][j] == 1:
            queue.append([i, j])

while queue:
    temp = []
    while len(queue) > 0:
        temp.append(queue.popleft())
    for cord in temp:
        a, b = cord[0], cord[1]
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < N and 0 <= y < M and box[x][y] == 0:
                queue.append([x,y])
                count += 1
                box[x][y] = 1
    answer +=1

if count == target:
    print(answer-1)
else:
    print(-1)