from collections import deque

N = int(input())
graph = []
answer = []
queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    graph.append(list(map(int, input().split())))

queue.append([0,0])

while queue:
    temp = []
    while len(queue) > 0:
        temp.append(queue.popleft)
    for cord in temp:
        a , b = cord[0], cord[1]
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < N and 0 <= y < N and graph[x][y] == 1:
                queue.append([x,y])