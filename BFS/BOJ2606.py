from collections import deque

node = int(input())
edge = int(input())

lst = []
for _ in range(edge):
    link = list(map(int, input().split()))
    lst.append([link[0],link[1]])
    
queue = deque()
queue.append(1)
visited = [False for _ in range(len(lst))]
answer = []

while len(queue) != 0:
    now = queue.popleft()
    if now not in answer:
        answer.append(now)
    for edge in range(len(lst)):
        if lst[edge][0] == now and visited[edge] == False:
            if lst[edge][1] not in queue:
                queue.append(lst[edge][1])
                visited[edge] = True
        elif lst[edge][1] == now and visited[edge] == False:
            if lst[edge][0] not in queue:
                queue.append(lst[edge][0])
                visited[edge] = True
print(len(answer) - 1)