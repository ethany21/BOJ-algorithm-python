from collections import deque

node = int(input())
edge = int(input())

lst = []
for _ in range(edge):
    link = list(map(int, input().split()))
    lst.append([link[0],link[1]])
    
queue = deque()
queue.append(1)
answer = 0

while len(queue) != 0:
    answer += 1
    now = queue.popleft()
    for edge in lst:
        if edge[0] == now:
            if edge[1] not in queue:
                queue.append(edge[1])
                
print(answer - 1)