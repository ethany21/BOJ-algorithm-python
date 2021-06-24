N = int(input())

day = []
dp = [0] * (N+1)

for i in range(N):
    day.append(list(map(int, input().split())))

for i in range(N):
    if i + day[i][0] <= N:
        dp[i + day[i][0]] = max(dp[i + day[i][0]], dp[i] + day[i][1])
    dp[i + 1] = max(dp[i+1], dp[i])

print(dp[N])