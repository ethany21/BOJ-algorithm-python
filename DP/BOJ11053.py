N = int(input())

arr = list(map(int, input().split()))

answer = [1 for _ in range(N)]

for i in range(N):
    temp = []
    for j in range(i):
        if arr[i] > arr[j]:
            temp.append(answer[j])
    if len(temp) > 0:
        answer[i] = max(temp) + 1

print(max(answer))