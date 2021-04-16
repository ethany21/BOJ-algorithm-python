import math

N = int(input())

def min_square(N):

    answer = []
    result = []
    limit = int(math.sqrt(N))

    if limit*limit == N:
        return 1
    else:
        for i in range(1, limit + 1):
            for j in range(i, limit + 1):
                if i*i + j*j == N and [i, j] not in answer:
                    answer.append([i, j])
                    if 2 in result:
                        continue
                    else:
                        result.append(2)
                else:
                    for k in range(j, limit + 1):
                        if i*i + j*j+ k*k== N and [i, j, k] not in answer:
                            answer.append([i, j, k])
                            if 3 in result:
                                continue
                            else:
                                result.append(3)
                        else:
                            for l in range(k, limit + 1):
                                if i*i + j*j + k*k + l*l == N and [i, j, k, l] not in answer:
                                    answer.append([i, j, k, l])
                                    if 4 in result:
                                        continue
                                    else:
                                        result.append(4)

        return min(result)
print(min_square(N))