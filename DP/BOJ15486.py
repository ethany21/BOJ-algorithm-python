N = int(input())

time, pay = [], []
dp = [0] * (1+N)

for _ in range(N):
    a,b = map(int, input().split())
    time.append(a)
    pay.append(b)

MAX = 0

for i in range(N):
    MAX = max(MAX, dp[i])
    if i + time[i] <= N:
        dp[i + time[i]] = max(MAX + pay[i], dp[i + time[i]])

print(max(dp))






# 규칙:
# 1. 앞에 있는게 페이가 더 크면 무조건 앞에 있는 걸 택한다
# 2. 만약 앞에 있는게 페이가 작더라도, 그 다음거 보다 일수가 작고, 
# 앞의 거 일수 끝나고 그 다음 일수와 더해서 작으면 앞에 있는 걸 택한다
# 3. 해당 과정은 N보다 그 합이 작아야 한다