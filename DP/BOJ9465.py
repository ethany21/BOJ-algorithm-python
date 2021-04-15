count = int(input())

stickers = [[] for _ in range(count)]
cols = []
answer = []

for i in range(count):
    cols.append(int(input()))
    for j in range(2):
        stickers[i].append(list(map(int, input().split())))



for case in stickers:

    temp = case

    for i in range(2):
        for j in range(len(case[0]) - 2):
            if i == 0:
                if case[i+1][j+1] + case[i][j+2] > case[i+1][j+2]:
                    temp[i][j + 2] += case[i+1][j+1] + case[i][j]
                    j += 2
                else:
                    temp[i +1][j + 2] += case[i][j]
                    i +=1
                    j += 2
            elif i == 1:
                if case[i-1][j+1] + case[i][j+2] > case[i-1][j+2]:
                    temp[i][j + 2] += case[i-1][j+1] + case[i][j]
                    j += 2
                else:
                    temp[i - 1][j + 2] += case[i][j]
                    i -=1
                    j +=2

    print(temp)

print(stickers)
        
