num = int(input())
target = int(input())
graph = [[0 for _ in range(num)]for _ in range(num)]

value = 1
direc = 1
count = 1

xtemp = int((num - 1)//2)
ytemp = int((num - 1)//2)
graph[xtemp][ytemp] = value

while value < pow(num, 2):
    if direc == 1:
        for i in range(count):
            value += 1
            xtemp -= 1
            graph[xtemp][ytemp] = value
            if value == num * num:
                break
        
        direc = 2
    elif direc == 2:
        for i in range(count):
            value += 1
            ytemp += 1
            graph[xtemp][ytemp] = value
        count += 1
        direc = 3
    
    elif direc == 3:
        for i in range(count):
            value += 1
            xtemp += 1
            graph[xtemp][ytemp] = value
        direc = 4

    elif direc == 4:
        for i in range(count):
            value += 1
            ytemp -= 1
            graph[xtemp][ytemp] = value
        count += 1
        direc = 1

for i in range(num):
    for j in range(num):
        print(graph[i][j], end=" ")
        if graph[i][j] == target:
            temp = [i+1, j+1]
    print()

print(temp[0], temp[1])