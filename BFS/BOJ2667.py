from collections import deque

N = int(input())
graph = []
answer = []
visited = []
queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    graph.append(list(map(int, input().split())))

for _ in range(N):
    visited.append([False for _ in range(N)])

for i in range(N):
    for j in range(N):
        visited[i][j] == True
        if graph[i][j] == 1 and not visited[i][j]:
            queue = deque()
            queue.append([i, j])
            count = 0
            while queue:
                temp = []
                while len(queue) > 0:
                    temp.append(queue.popleft())
                for cord in temp:
                    a , b = cord[0], cord[1]
                    for i in range(4):
                        x = a + dx[i]
                        y = b + dy[i]
                        if 0 <= x < N and 0 <= y < N and graph[x][y] == 1 and not visited[a][b]:
                            graph[a][b] = True
                            queue.append([x, y])
                            count +=1
            answer.append(count)
print(answer)