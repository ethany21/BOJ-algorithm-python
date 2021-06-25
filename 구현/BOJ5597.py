check = [i for i in range(1, 31)]

for _ in range(28):
    hand = int(input())
    del check[hand - 1]
for i in check:
    print(i)
