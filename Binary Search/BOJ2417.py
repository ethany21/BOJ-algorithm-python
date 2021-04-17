from math import pow

N = int(input())

def solution(N):
    i = 0
    M = N/2

    if N in [0,1]:
        return N
        
    else:
        while i <= M:
            mid = int((i + M)/2)

            if pow(mid, 2) > N:
                M = mid - 1
            elif pow(mid-1, 2) < N:
                i = mid + 1

        if pow(M, 2) >= N:
            return M
        else:
            return i

print(solution(N))
