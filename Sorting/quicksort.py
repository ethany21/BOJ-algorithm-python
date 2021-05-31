lst = list(map(int, input().split()))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    less, equal, more = [], [], []
    for i in arr:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            more.append(i)
        else:
            equal.append(i)
    return quick_sort(less) + equal + quick_sort(more)

def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end

    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and pivot <= arr[right]:
            right -= 1
        if left > right:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    return right

def quicksort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quicksort(arr, start, pivot-1)
        quicksort(arr, pivot+1, end)
    return arr

print(quicksort(lst, 0, len(lst) - 1))

print(quick_sort(lst))