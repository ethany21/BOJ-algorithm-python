# N = int(input())

array = [1, 2, 3]
visited = [False for _ in range(3)]

cand = []

## temp는 리스트로, 쌓으면서 앞 원소들과 비교해 본다
def dfs(visited, N, count, temp):
    pass

def check(temp):

    result = False

    for i in range(int(len(temp)/2)):
        front = temp[-i*2:-i]
        back = temp[-i:-1]
        if front == back:
            result = True
            break

    return result

print(int(3/2))
print(check([1,3,3]))

