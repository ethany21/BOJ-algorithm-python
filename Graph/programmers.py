import sys

def solution(n, edge):
    answer = 0
    
    d = []
    
    for i in range(n):
        d.append([sys.maxsize for _ in range(n)])
    
    for i in edge:
        i.sort()
    
    for i in range(n):
        for j in range(n):
            if [i+1, j+1] in edge:
                d[i][j] = 1
                d[j][i] = 1
    
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    temp = d[0]
    del temp[0]
    
    answer = temp.count(max(temp))

    return answer