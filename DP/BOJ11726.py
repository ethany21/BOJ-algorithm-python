N = int(input())

answers = [1, 2]
for i in range(2, N):
  answers.append(answers[i-2] + answers[i-1])

print(answers[N-1]%10007)