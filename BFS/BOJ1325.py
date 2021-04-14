#데이터 입력 받아오기
#node는 컴퓨터의 개수, edge는 연결 간선의 개수
import sys
node, edge = map(int, sys.stdin.readline().split())

#graph에다가 edge 개수만큼의 입력을 받아온다
graph = []
for _ in range(edge):
    graph.append(list(map(int, sys.stdin.readline().split())))