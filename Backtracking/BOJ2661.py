N = int(input())

cand = []
array = [1, 2, 3]

def check(temp):

    result = False

    for i in range(1,int(len(temp)/2) + 1):
        front = temp[-i*2:-i]
        back = temp[-i:]
        if front == back:
            result = True
            break

    return result   

def dfs(N, temp):

    if len(cand) == 1:
        return

    if len(temp) == N:
        answer = "".join([str(_) for _ in temp])
        cand.append(int(answer))
        return

    for i in range(3):
        temp.append(array[i])
        if not check(temp):
            dfs(N, temp)
        del temp[-1]  
        
dfs(N, [])
print(cand[0])