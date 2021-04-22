N, M = map(int, input().split())

lst = [i for i in range(1, N+1)]
answers = []
visited = [False for _ in range(N)]

def dfs(visited, lst, count, temp, idx):

    container = []

    if len(temp) == count:
        for i in temp:
            container.append(i)
        answers.append(container)
        return

    else:
        for i in range(idx, len(lst)):
            if lst[i] not in temp and not visited[i]:
                temp.append(lst[i])
                visited[i] = True
                dfs(visited, lst, count, temp, idx)
                del temp[-1]
                visited[i] = False
            idx += 1q

dfs(visited, lst, M, [], 0)

for i in answers:
    for j in i:
        print(j, end= " ")
    print("")