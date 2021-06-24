from collections import deque

N, L, R = map(int, input().split())
populations = []

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    populations.append(list(map(int, input().split())))

def bfs(i, j):
    visited[i][j] = 1
    q = deque()
    q.append([i,j])
    temp = []
    temp.append([i, j])

    while q:
        x, y = q.popleft()
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < N and 0 <= b < N and visited[a][b] == 0:
                if L <= abs(populations[a][b] - populations[x][y]) <= R:
                    visited[a][b]= 1
                    q.append([a,b])
                    temp.append([a,b])
    return temp
cnt = 0
while True:
    visited = [[0]*N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                temp = bfs(i,j)
                if len(temp) > 1:
                    flag = True
                    num = sum(populations[x][y] for x,y in temp)//len(temp)
                    for x, y in temp:
                        populations[x][y] = num
    if flag == False:
        break
    cnt +=1
print(cnt)