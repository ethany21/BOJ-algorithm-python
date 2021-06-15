def solution(distance, rocks, n):
    answer = 0

    rocks.append(distance)
    rocks.append(0)

    rocks.sort()

    difference = []

    for i in range(1, len(rocks)):
        difference.append(rocks[i] - rocks[i-1])

    return answer

solution(25, [2, 14, 11, 21, 17], 2)