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

# for문을 4번이 아니라, 3번만 돌아도 충분하다
# 왜냐면 3개의 수의 제곱수의 합으로 만들 수 없다면 
# 자동으로 4개의 제곱수로 만들 수 있다는 것을 이미 문제를 통해 알 수 있다
# 이미 증명이 되어 있는 사실이므로 3번까지만 순회하고 제곱수의 합으로 만들 수 없다면 4를 return 하면 된다

    if len(result) == 0:
        return 4
    else:
        return min(result)
print(min_square(N))