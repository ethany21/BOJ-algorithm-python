import sys
from collections import deque

# 데이터 입력 받아오기
# node는 컴퓨터의 개수, edge는 연결 간선의 개수
node, edge = map(int, sys.stdin.readline().split())

# graph에다가 edge 개수만큼의 입력을 받아온다
graph = []
for _ in range(edge):
    graph.append(list(map(int, sys.stdin.readline().split())))

visited = [False for _ in range(edge)]

dic = {}
for i in range(1, node+1):
    dic[i] = [i]

def bfs(start):
    visited = [False for _ in range(edge)]
    queue = deque()
    queue.append(start)
    while len(queue) != 0:
        now = queue.popleft()
        for i in range(len(graph)):
            if graph[i][1] == now and visited[i] == False:
                dic[start].append(graph[i][0])
                queue.append(graph[i][0])
                visited[i] =True

for i in range(1, node+1):
    bfs(i)

max = 0
answer = []
for i in dic.keys():
    if len(dic[i]) > max:
        max = len(dic[i])
for i in dic.keys():
    if len(dic[i]) == max:
        answer.append(i)
answer.sort()
for i in answer:
    print(i, end=' ')