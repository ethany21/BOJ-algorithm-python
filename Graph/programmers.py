from collections import deque

def solution(n, edge):
    
    answer = 0
    dic = {}
    dist = 0
    visited = [False for _ in range(n)]
    queue = deque()
    count = 0
    distance = {}
    
    for i in range(1, n+1):
        for j in range(len(edge)):
            if i in edge[j]:
                value = 0
                if edge[j][0] == i:
                    value = edge[j][1]
                else:
                    value = edge[j][0]
                if i not in dic.keys():
                    dic[i] = [value]
                else:
                    dic[i].append(value)
    
    queue.append(1)
    
    while queue:
        temp = []
        while len(queue) > 0:
            temp.append(queue.popleft())
            
        for node in temp:
            if not visited[node-1]:
                visited[node-1] = True
            
            distance[node] = count
            
            for i in dic[node]:
                if not visited[i-1]:
                    queue.append(i)
                    visited[i-1] = True
        count += 1
    
    max_value = max(distance.values())
    
    for i in range(1, n+1):
        if distance[i] == max_value:
            answer +=1
    
    return answer