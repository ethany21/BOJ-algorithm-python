def counting_sorted(arr, k):
    c = [0] * k

    sorted_arr = [0] * len(arr)

    for i in arr:
        c[i] += 1

    for i in range(1, k):
        c[i] += c[i-1]
    
    for i in range(len(arr)):
        sorted_arr[c[arr[i]] - 1] = arr[i]
        c[arr[i]] -= 1

    return sorted_arr

arr = [9, 1, 22, 4, 0, 1, 23, 22, 29, 9]

print(counting_sorted(arr, max(arr)+1))
