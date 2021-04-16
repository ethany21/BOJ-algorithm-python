N = int(input())

count3 = int(N / 3) + 1
count5 = int(N / 5) + 1

answer = []

for i in range(count3):
    for j in range(count5):
        if i*3 + j*5 == N:
            answer.append(i+j)

if len(answer) == 0:
    print(-1)
else:
    print(min(answer))