N = int(input())
def solution(N):

    if N in [1, 2]:
        return 1
    elif N == 3:
        return 2
    else:
        answer = 0
        for i in range(N):
            if (i*(i+1))/2 > N:
                answer = i
                break
        return answer - 1
print(solution(N))
