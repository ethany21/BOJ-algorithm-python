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