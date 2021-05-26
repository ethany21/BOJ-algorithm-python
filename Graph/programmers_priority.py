import sys

def solution(n, results):
    answer = 0
    dic = {}
    graph = []
    
    for i in range(1, n+1):
        dic[i] = 0
    
    for i in range(n):
        graph.append([sys.maxsize for _ in range(n)])
    
    for i in range(n):
        for j in range(n):
            if [i+1,j+1] in results:
                graph[i][j] = 1
                
    # 플로이드 워셜로 각 노드 간의 최소 거리를 기록하고,
    # sys.maxsize가 아닌 경우의 값인 경우라면, 노드 간 이동이 가능한 것으로 간주

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    
    for i in range(1,n+1):
        count = 0
        for j in range(1,n+1):
            if graph[i-1][j-1] is not sys.maxsize:
                count +=1
            elif graph[j-1][i-1] is not sys.maxsize:
                count +=1
        dic[i] = count
    
    for i in dic:
        if dic[i] == n-1:
            answer +=1
    
    return answer