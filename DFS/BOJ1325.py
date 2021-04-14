#데이터 입력 받아오기
#node는 컴퓨터의 개수, edge는 연결 간선의 개수
import sys
node, edge = map(int, sys.stdin.readline().split())

#graph에다가 edge 개수만큼의 입력을 받아온다
graph = []
for _ in range(edge):
    graph.append(list(map(int, sys.stdin.readline().split())))
    
# node 개수 만큼의 컴퓨터가 있을 때,
# 한 컴퓨터가 총 해킹할 수 있는 컴퓨터를 값으로 넣기 위한 dictionary
# 

dic = {}
for i in range(1, node+1):
    # 우선, 한 컴퓨터에서 해킹을 시작하면, 컴퓨터 자신은 해킹이 되므로 이렇게 초기화
    # dic = {1:[1], 2:[2], 3:[3] ... 5:[5]}
    dic[i] = [i]

# 기존엔 visited가 dfs 함수 안에 있었다면, 이를 전역 변수화 하고 dfs 파라미터에 추가했다
# cycle이 입력으로 들어 올 시는 해결되었다 (아닐수도.....)
visited = [False for _ in range(edge)]

# 백트래킹 방식으로 위에서 입력으로 받아오고 만든 graph를 순회한다
def dfs(graph, first, original, visited):
    count = 0
    for i in visited:
        if i == True:
            count += 1
    if count == len(visited):
        return

    for i in range(edge):
        if graph[i][1] == first and not visited[i]:

            dic[original].append(graph[i][0])
            # dic[original] += 1
            first = graph[i][0]
            visited[i] = True
            dfs(graph, first, original, visited)
            first = graph[i][1]
            visited[i] = False

# node 개수의 컴퓨터만큼 순회를 돌면서, dictionay에 각 key node마다 해킹할 수 있는 컴퓨터를 append한다
for i in range(1, node+1):
    dfs(graph, i, i, visited)

# 해킹 가능한 컴퓨터의 개수 중 가장 최댓값을 찾는다
max = 0
for i in dic.keys():
    if len(dic[i]) > max:
        max = len(dic[i])

# 해킹 가능한 컴퓨터의 수가 max와 동일한 컴퓨터를 찾고 answer에 추가한다
answer = []
for i in dic.keys():
    if len(dic[i]) == max:
        answer.append(i)

# answer을 정렬하고, 옆으로 출력한다
answer.sort()
for i in answer:
    print(i, end=' ')