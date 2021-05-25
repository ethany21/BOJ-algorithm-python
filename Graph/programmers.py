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
        dic[i] = []
    
    for i in edge:
        dic[i[0]].append(i[1])
        dic[i[1]].append(i[0])
    
    queue.append(1)
    
    while queue:
        
        if visited.count(True) == n:
            answer = len(queue)
            break
        
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
    
    return answer