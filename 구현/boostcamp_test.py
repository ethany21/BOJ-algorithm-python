

def solution(lst):

    dic = {}
    result = []

    for i in lst:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
    for i in dic.keys():
        if dic[i] > 1:
            result.append(dic[i])

    if len(result) > 0:
        return result
    else:
        return [-1]

print(solution([3,2,4,4,2,5,2,5,5]))
print(solution([3,5,7,9,1]))