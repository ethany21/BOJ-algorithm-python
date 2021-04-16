from math import factorial as fac

N = int(input())

tests = []
for _ in range(N):
    tests.append(list(map(int, input().split())))

answers = []
for site in tests:
    
    answers.append(int(fac(site[1]) / (fac(site[0]) * fac(site[1] - site[0]))))

for i in answers:
    print(i)
