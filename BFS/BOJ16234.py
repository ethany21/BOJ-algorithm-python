from collections import deque

N, L, R = map(int, input().split())

populations = []
queue = deque()
visited = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    populations.append(list(map(int, input().split())))

for _ in range(N):
    visited.append([False for _ in range(N)])

def check(current):

    adjacent = []

    return adjacent

def bfs():
    pass

while True:
    for i in range(N):
        for j in range(N):
            pass