from collections import deque

N, L, R = map(int, input().split())

populations = []
queue = deque()
visited = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    populations.append(list(map(int, input().split())))
queue.append([0,0])

for _ in range(N):
    visited.append([False for _ in range(N)])

count = 1
while queue:
    temp = []
    while len(queue) > 0:
        temp.append(queue.popleft())
    for cord in temp:
        a , b = cord[0], cord[1]
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < N and 0 <= y < N and populations[x][y] == 1 and not visited[x][y]:
                visited[x][y] = True
                queue.append([x, y])
                count +=1