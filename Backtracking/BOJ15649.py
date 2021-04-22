N, M = map(int, input().split())

lst = [i for i in range(1, N + 1)]
visited = [False for _ in range(len(lst))]
answers = []

def dfs(visited, lst, count, temp):

    container = []

    if len(temp) == count:
        for i in temp:
            container.append(i)
        answers.append(container)
        return

    else:
        for j in range(len(lst)):
            if lst[j] not in temp and not visited[j]:
                temp.append(lst[j])
                visited[j] = True
                dfs(visited, lst, count, temp)
                del temp[-1]
                visited[j] = False

dfs(visited, lst, M, [])

for i in answers:
    for j in i:
        print(j, end= " ")
    print("")

