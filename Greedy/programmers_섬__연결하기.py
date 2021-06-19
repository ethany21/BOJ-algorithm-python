def solution1(n, costs):
    answer = 0
    
    visited = [0] * n

    costs.sorted(key = lambda x: x[2])

    visited[0] = 1

    while sum(visited) != n:
        for cost in costs:
            start, end, c = cost
            if visited[start] == 1 or visited[end] == 1:
                if visited[start] == 1 and visited[end] == 1:
                    continue
                else:
                    visited[start] = 1
                    visited[end] = 1
                    answer += c
                    break
    return answer

def ancestor(parents, node):
    if parents[node] == node:
        return node
    else:
        return ancestor(parents, parents[node])

def solution2(n, costs):

    answer = 0


    return answer