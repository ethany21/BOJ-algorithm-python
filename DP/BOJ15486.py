N = int(input())

schedule = []

for _ in range(N):
    schedule.append(list(map(int, input().split())))

pay = 0





# 규칙:
# 1. 앞에 있는게 페이가 더 크면 무조건 앞에 있는 걸 택한다
# 2. 만약 앞에 있는게 페이가 작더라도, 그 다음거 보다 일수가 작고, 
# 앞의 거 일수 끝나고 그 다음 일수와 더해서 작으면 앞에 있는 걸 택한다
# 3. 해당 과정은 N보다 그 합이 작아야 한다