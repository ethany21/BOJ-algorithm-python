from collections import deque

N = int(input())
graph = []
answer = []
visited = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    graph.append(list(map(int, input())))

for _ in range(N):
    visited.append([False for _ in range(N)])

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            queue = deque()
            queue.append([i, j])
            count = 1
            while queue:
                temp = []
                while len(queue) > 0:
                    temp.append(queue.popleft())
                for cord in temp:
                    a , b = cord[0], cord[1]
                    for i in range(4):
                        x = a + dx[i]
                        y = b + dy[i]
                        if 0 <= x < N and 0 <= y < N and graph[x][y] == 1 and not visited[x][y]:
                            visited[x][y] = True
                            queue.append([x, y])
                            count +=1
            answer.append(count)
answer.sort()
print(len(answer))
for i in answer:
    print(i)
