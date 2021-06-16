def solution(distance, rocks, n):
    answer = 0

    rocks.append(distance)
    rocks.append(0)
    rocks.sort()
        
    left, right = 0, distance
    
    while left <= right:
        
        mid = (left + right)//2
        pivot = 0
        removal = 0
        
        for i in range(1, len(rocks)):
            if rocks[i] - rocks[pivot] < mid:
                removal += 1
            else:
                pivot = i
                
        if removal >= n:
            answer = mid
            right = mid - 1
            
        elif removal < n:
            left = mid + 1

    return answer